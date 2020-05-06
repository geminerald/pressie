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
# bcrypt = Bcrypt(app)


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
            return redirect(url_for('profile', user=user_in_db['username']))

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
    flash('You were logged out!')
    return redirect(url_for('home'))

# Profile Page
@app.route('/profile/<user>')
def profile(user):
    # Check if user is logged in
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = mongo.db.users.find_one({"email": user})
        user_lists = mongo.db.lists.find({"list_username": user_in_db["email"]})
        return render_template('profile.html', wishlists=user_lists, user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('home'))


"""
About function - returns about page
"""


@app.route('/about')
def about():
    return render_template('about.html', title='About')


"""
Finder function - returns find wishlist page for buyers.
"""


@app.route('/finder')
def finder():
    return render_template('finder.html', title='Find a Wishlist')


"""
Wishlist function - returns wishlist page for listers and allows them to create a new one.
"""


@app.route('/wishlist/<user>')
def wishlist(user):
    if 'user' in session:
        user_in_db = mongo.db.users.find_one({"email": user})
        if user_in_db:
            # If so redirect user to his profile
            flash("You are logged in already!")
            return render_template('wishlist.html', title='Create a Wishlist', user=user_in_db)
    else:
        # Render the page for user to be able to log in
        return render_template("login.html", form=LoginForm())
    


"""
Insert Wishlist function - takes user data from wishlist page and inserts to db. Then redirects to profile (likely to be changed to add items.)
"""


@app.route('/insertwishlist/<user>', methods=['GET', 'POST'])
def insert_wishlist(user):
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = mongo.db.users.find_one({"email": user})
        lists = mongo.db.lists
        lists.insert_one(request.form.to_dict())
        return render_template('profile.html', user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('home'))


"""
View Wishlist function - returns wishlist html page and all associated items.
"""


@app.route('/viewwishlist/<list_id>')
def view_wishlist(list_id):
    myquery = {"list_id": list_id}
    items = mongo.db.items.find(myquery)
    pass_in_list_id = list_id
    return render_template('viewwishlist.html', items=items, list_id=pass_in_list_id)


"""
Edit Wishlist function - returns wishlist page for listers and allows them to update existing one.
"""
@app.route('/editwishlist/<list_id>')
def edit_wishlist(list_id):
    the_list = mongo.db.lists.find_one({"_id": ObjectId(list_id)})
    return render_template('editlist.html', the_list=the_list)


"""
Delete Wishlist function - Permanently deletes wishlist.
"""


@app.route('/deletewishlist/<list_id>')
def delete_wishlist(list_id):
    mongo.db.lists.remove({'_id': ObjectId(list_id)})
    return redirect(url_for('profile'))


"""
Update Wishlist function - Updates basic wishlist parameters in the DB.
"""


@app.route('/updatewishlist/<list_id>', methods=["GET", "POST"])
def update_wishlist(list_id):
    lists = mongo.db.lists
    lists.update({'_id': ObjectId(list_id)},
                 {
        'phone_number': request.form.get('phone_number'),
        'list_username': request.form.get('list_username'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name')
    })
    return redirect(url_for('profile'))


"""
Add Items function - Adds items to a specific wishlist. 

Parameters: List Id - this is used to add the items to the db with a specific wishlist.

"""
@app.route('/additems/<list_id>')
def additems(list_id):
    the_list = mongo.db.lists.find_one({"_id": ObjectId(list_id)})
    the_list_id = the_list['_id']
    return render_template('additems.html', title='Add Items to your Wishlist', item_list_id=the_list_id)


"""
Insert Items function - Adds items to db from user form. 
"""


@app.route('/insertitems', methods=['GET', 'POST'])
def insert_items():
    items = mongo.db.items
    items.insert_one(request.form.to_dict())
    return redirect('profile')


"""
Delete Item function - Permanently deletes Item.
"""


@app.route('/deleteitem/<item_id>')
def delete_item(item_id):
    the_item = mongo.db.items
    the_list = the_item.list_id
    the_item.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('view_wishlist', list_id=the_list))


"""
List Search function - Takes a buyer to their desiered wishlist for someone they want to buy for. 
"""
@app.route('/listsearch')
def list_search():
    user = request.form.get('search')
    the_list = mongo.db.lists.find_one({'phone_number': user})
    return redirect(url_for('view_wishlist', list_id=the_list))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
