import os
from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    # Check if user is not logged in already
    if 'user' in session:
        user_in_db = mongo.db.users.find_one({"email": session['user']})
        if user_in_db:
            # If so redirect user to his profile
            flash("You are logged in already!")
            return redirect(url_for('profile', user=user_in_db['email']))
    else:
        # Render the page for user to be able to log in
        return render_template("login.html", form=LoginForm())

# Check user login details from login form
@app.route('/user_auth', methods=['POST'])
def user_auth():
    form = request.form.to_dict()
    user_in_db = mongo.db.users.find_one({"email": form['email']})
    # Check for user in database
    if user_in_db:
        # If passwords match (hashed / real password)

        # Changed this
        # if check_password_hash(user_in_db['password'], form['password']):
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), user_in_db['password']) == user_in_db['password']:
            # Log user in (add to session)
            session['user'] = form['email']
            # If the user is admin redirect him to admin area

            flash("You were logged in!", 'success')
            return redirect(url_for('profile', user=user_in_db['email']))

        else:
            flash("Wrong password or user name!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))

# Sign up
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already sign in!')
        return redirect(url_for('home'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if the password and password1 actualy match
        if form['password'] == form['confirm_password']:
            # If so try to find the user in db
            user = mongo.db.users.find_one({"username": form['username']})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for('register'))
            # If user does not exist register new user
            else:
                # Hash password
                hash_pass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), bcrypt.gensalt())
                # Create new user with hashed password
                mongo.db.users.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_pass
                    }
                )
                # Check if user is actualy saved
                user_in_db = mongo.db.users.find_one(
                    {"username": form['username']})
                if user_in_db:
                    # Log user in (add to session)
                    session['user'] = user_in_db['email']
                    return redirect(url_for('profile', user=user_in_db['email']))
                else:
                    flash("There was a problem savaing your profile")
                    return redirect(url_for('register'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('register'))

    return render_template("register.html", form=RegistrationForm())

# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!', 'success')
    return redirect(url_for('home'))

# Profile Page
@app.route('/profile/<user>')
def profile(user):
    # Check if user is logged in
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = mongo.db.users.find_one({"email": user})
        user_lists = mongo.db.lists.find(
            {"list_username": user_in_db["email"]})
        return render_template('profile.html', wishlists=user_lists, user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('home'))


# About Page
@app.route('/about')
def about():
    # Return about page html - nothing fancy.
    return render_template('about.html', title='About')


# Wishlist Finder Page
@app.route('/finder')
def finder():
    # Locate a wishlist using a number.
    return render_template('finder.html', title='Find a Wishlist')


# Create a new Wishlist Page
@app.route('/wishlist/<user>')
def wishlist(user):
    # Checks for logged in user
    if 'user' in session:
        # If so takes session info
        user_in_db = mongo.db.users.find_one({"email": user})
        if user_in_db:
            # If so redirect user to his wishlist html page and capture session
            flash("You are logged in already!")
            return render_template('wishlist.html', title='Create a Wishlist', user=user_in_db)
    else:
        # Render the page for user to be able to log in
        return render_template("login.html", form=LoginForm())


# Insert wishlist to DB from form
@app.route('/insertwishlist/<user>', methods=['GET', 'POST'])
def insert_wishlist(user):
    # Confirms user is logged in
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = mongo.db.users.find_one({"email": user})
        lists = mongo.db.lists
        lists.insert_one(request.form.to_dict())
        return redirect(url_for('profile', user=user_in_db['email']))
    else:
        # Otherwise redirects to login page
        flash("You must be logged in!")
        return redirect(url_for('home'))


# View an individual wishlist's items
@app.route('/viewwishlist/<list_id>')
def view_wishlist(list_id):
    # Gets the Wishlist ID
    myquery = {"list_id": list_id}
    # Checks for it in the DB
    items = mongo.db.items.find(myquery)
    pass_in_list_id = list_id
    # passes both into the template
    return render_template('viewwishlist.html', items=items, list_id=pass_in_list_id)


# Page to get list info and be able to edit it.
@app.route('/editwishlist/<list_id>')
def edit_wishlist(list_id):
    the_list = mongo.db.lists.find_one({"_id": ObjectId(list_id)})
    return render_template('editlist.html', the_list=the_list)


# Remove a wishlist from the database
@app.route('/deletewishlist/<user>/<list_id>')
def delete_wishlist(user, list_id):
    # Takes User and list ID
    if 'user' in session:
        # Confirms user is logged in - if so removes the specified wishlist
        # from the DB and redirects back to the profile page with the user info
        mongo.db.lists.remove({'_id': ObjectId(list_id)})
        user_in_db = mongo.db.users.find_one({"email": session['user']})
        user_lists = mongo.db.lists.find(
            {"list_username": user_in_db["email"]})
        return redirect(url_for('profile', wishlists=user_lists, user=user))
    else:
        # If not logged in will redirect back to login page with appropriate alert.
        flash("You must be logged in!", 'alert')
        return redirect(url_for('login'))


# Update a wishlist in the database
@app.route('/updatewishlist/<list_id>', methods=["GET", "POST"])
def update_wishlist(list_id):
    # Get the wishlist by ID
    lists = mongo.db.lists
    # Update it based on the form
    lists.update({'_id': ObjectId(list_id)},
                 {
        'phone_number': request.form.get('phone_number'),
        'list_username': request.form.get('list_username'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name')
    })
    # Redirect back to profile.
    return redirect(url_for('profile'))


# Page where one can add items to a wishlist in the DB
@app.route('/additems/<list_id>')
def additems(list_id):
    # Get list to add to by passed in ID
    the_list = mongo.db.lists.find_one({"_id": ObjectId(list_id)})
    the_list_id = the_list['_id']
    # Pass into html page
    return render_template('additems.html', title='Add Items to your Wishlist', item_list_id=the_list_id)


# Function to write to db
@app.route('/insertitems', methods=['GET', 'POST'])
def insert_items():
    # insert items into items collection in db
    items = mongo.db.items
    items.insert_one(request.form.to_dict())
    # and redirect to profile.
    return redirect('profile')


# Function to permanently delete an item .
@app.route('/deleteitem/<item_id>')
# get item by ID
def delete_item(item_id):
    # locate item in DB
    the_item = mongo.db.items
    the_list = the_item.list_id
    # Remove item - TODO: update to mark for archive for a period of time.
    the_item.remove({'_id': ObjectId(item_id)})
    # return to the wishlist.
    return redirect(url_for('view_wishlist', list_id=the_list))


# Search for a list from Finder page form.
@app.route('/listsearch')
def list_search():
    form = request.form.to_dict()
    the_list = mongo.db.lists.find({"phone_number": form["search"]})
    return redirect(url_for('view_wishlist', list_id=the_list))


# Main Init function - currently in development mode. TODO update to debug is false
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
