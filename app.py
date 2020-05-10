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

#Collections:

users_collection = mongo.db.users
lists_collection = mongo.db.lists
items_collection = mongo.db.items


@app.route('/')
def home():
    """Renders the home page template"""
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    """ Logs a user in"""
    if 'user' in session:
        user_in_db = users_collection.find_one({"email": session['user']})
        if user_in_db:

            flash("You are logged in already!")
            return redirect(url_for('profile', user=user_in_db['email']))
    else:

        return render_template("login.html", form=LoginForm())


@app.route('/user_auth', methods=['POST'])
def user_auth():
    """Check's a user's credentials against the db"""
    form = request.form.to_dict()
    user_in_db = users_collection.find_one({"email": form['email']})

    if user_in_db:

        if bcrypt.hashpw(request.form['password'].encode('utf-8'), user_in_db['password']) == user_in_db['password']:
            session['user'] = form['email']
            flash("You were logged in!", 'success')
            return redirect(url_for('profile', user=user_in_db['email']))

        else:
            flash("Wrong password or user name!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Creates a new user in the DB"""
    if 'user' in session:
        flash('You are already sign in!')
        return redirect(url_for('home'))
    if request.method == 'POST':
        form = request.form.to_dict()
        if form['password'] == form['confirm_password']:
            user = users_collection.find_one({"username": form['username']})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for('register'))
            else:
                hash_pass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users_collection.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_pass
                    }
                )
                user_in_db = users_collection.find_one(
                    {"username": form['username']})
                if user_in_db:
                    session['user'] = user_in_db['email']
                    return redirect(url_for('profile', user=user_in_db['email']))
                else:
                    flash("There was a problem savaing your profile")
                    return redirect(url_for('register'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('register'))

    return render_template("register.html", form=RegistrationForm())


@app.route('/logout')
def logout():
    """Clears the user session"""
    session.clear()
    flash('You were logged out!', 'success')
    return redirect(url_for('home'))


@app.route('/profile/<user>')
def profile(user):
    """Shows profile page for user in session"""
    if 'user' in session:
        user_in_db = users_collection.find_one({"email": user})
        user_lists = lists_collection.find(
            {"list_username": user_in_db["email"]})
        return render_template('profile.html', wishlists=user_lists, user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('home'))


@app.route('/about')
def about():
    """Shows the about page"""
    return render_template('about.html', title='About')


@app.route('/finder')
def finder():
    """Shows the find a wishlist page"""
    return render_template('finder.html', title='Find a Wishlist')


@app.route('/wishlist/<user>', methods=['GET', 'POST'])
def wishlist(user):
    """Page to add and insert wishlist into db"""
    if 'user' in session:
        if request.method == "POST":
            user_in_db = users_collection.find_one({"email": user})
            lists = lists_collection
            lists.insert_one(request.form.to_dict())
            return redirect(url_for('profile', user=user_in_db['email']))
        else:
            user_in_db = users_collection.find_one({"email": user})
            if user_in_db:
                flash("You are logged in already!")
                return render_template('wishlist.html', title='Create a Wishlist', user=user_in_db)
    else:
        return render_template("login.html", form=LoginForm())


@app.route('/viewwishlist/<list_id>')
def view_wishlist(list_id):
    """View a specific wishlist"""
    myquery = {"list_id": list_id}
    items = items_collection.find(myquery)
    pass_in_list_id = list_id
    return render_template('viewwishlist.html', items=items, list_id=pass_in_list_id)


@app.route('/editwishlist/<list_id>')
def edit_wishlist(list_id):
    """Update a wishlist in the DB"""
    the_list = lists_collection.find_one({"_id": ObjectId(list_id)})
    return render_template('editlist.html', the_list=the_list, user=session['user'])


@app.route('/deletewishlist/<user>/<list_id>')
def delete_wishlist(user, list_id):
    """Removes a wishlist from the DB"""
    if 'user' in session:
        lists_collection.remove({'_id': ObjectId(list_id)})
        items_collection.remove({'list_id': ObjectId(list_id)})
        user_in_db = users_collection.find_one({"email": session['user']})
        user_lists = lists_collection.find(
            {"list_username": user_in_db["email"]})
        return redirect(url_for('profile', wishlists=user_lists, user=user))
    else:
        flash("You must be logged in!", 'alert')
        return redirect(url_for('login'))


@app.route('/updatewishlist/<list_id>', methods=["GET", "POST"])
def update_wishlist(list_id):
    """Updates record in the DB"""
    lists = lists_collection
    lists.update({'_id': ObjectId(list_id)},
                 {
        'phone_number': request.form.get('phone_number'),
        'list_username': request.form.get('list_username'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name')
    })
    return redirect(url_for('profile', user=request.form.get('list_username')))


@app.route('/additems/<list_id>')
def additems(list_id):
    """Shows the add items page"""
    the_list = lists_collection.find_one({"_id": ObjectId(list_id)})
    the_list_id = the_list['_id']
    return render_template('additems.html', title='Add Items to your Wishlist', item_list_id=the_list_id)


@app.route('/insertitems', methods=['GET', 'POST'])
def insert_items():
    """Adds items to the db"""
    items = items_collection
    items.insert_one(request.form.to_dict())
    list_id = request.form['list_id']
    return redirect(url_for('view_wishlist', list_id=list_id))


@app.route('/deleteitem/<item_id>')
def delete_item(item_id):
    """Removes an item from the DB"""
    the_item = items_collection
    the_list = the_item.list_id
    the_item.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('view_wishlist', list_id=the_list))


@app.route('/listsearch', methods=["GET"])
def list_search():
    """Locates a specific wishlist from info entered"""
    list_search = request.form.get('list_search')
    the_list = list(lists_collection.find({'phone_number': list_search}))
    list_id = the_list
    if list_id:
        flash('List Located!', 'success')
        return redirect(url_for('view_wishlist', list_id=list_id))
    else:
        flash('No list located for that number', 'info')
        return redirect(url_for('finder'))


# Main Init function - currently in development mode. TODO update to debug is false
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get(
        'PORT'), debug=os.environ.get('DEBUG'))
