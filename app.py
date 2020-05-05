import os
import datetime
import uuid
from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, redirect, request, url_for, flash, session, make_response
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


class User(UserMixin):

    def __init__(self, username, email, password, _id=None):

        self.username = username
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

    @classmethod
    def get_by_username(cls, username):
        data = mongo.db.users.find_one({"username": username})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_email(cls, email):
        data = mongo.db.users.find_one({"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = mongo.db.users.find_one({"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        verify_user = User.get_by_email(email)
        if verify_user is not None:
            return bcrypt.check_password_hash(verify_user.password, password)
        return False

    @classmethod
    def register(cls, username, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(username, email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        mongo.db.users.insert(self.json())


@app.route('/')
def home():
    return render_template('index.html', title='Home')


"""
Register function - takes register form info, adds to db and updates user to logged in.

Currently bugged.
"""


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            username = request.form["username"]
            email = request.form["email"]
            password = bcrypt.generate_password_hash(
                request.form["password"]).decode('utf-8')
            find_user = User.get_by_email(email)
            if find_user is None:
                User.register(username, email, password)
                flash(f'Account created for {form.username.data}!', 'success')
                return redirect(url_for('home'))
            else:
                flash(
                    f'Account already exists for {form.username.data}!', 'success')
    return render_template('register.html', title='Register', form=form)


"""
Login function - takes user login info and sets to logged in

Currently bugged
"""


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form["email"]
        password = request.form["password"]
        find_user = mongo.db.users.find_one({"email": email})
        if User.login_valid(email, password):
            loguser = User(find_user["_id"],
                           find_user["email"], find_user["password"])
            login_user(loguser, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


"""
User loader function - returns user ID for login attempt. Needed for flask-login
"""


@login_manager.user_loader
def load_user(user_id):
    user = User.get_by_id(user_id)
    if user is not None:
        return User(user["_id"])
    else:
        return None


@app.route("/logout")
@login_required
def logout():
    logout_user()
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


@app.route('/wishlist')
def wishlist():
    users = mongo.db.users.find()
    return render_template('wishlist.html', title='Create a Wishlist', users=users)


"""
Insert Wishlist function - takes user data from wishlist page and inserts to db. Then redirects to profile (likely to be changed to add items.)
"""


@app.route('/insertwishlist', methods=['GET', 'POST'])
def insert_wishlist():
    lists = mongo.db.lists
    lists.insert_one(request.form.to_dict())
    return redirect(url_for('profile'))


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
Profile function - Takes user to their profile page where they can view and update their info and lists.
"""


@app.route('/profile')
@login_required
def profile():
    my_account = mongo.db.users.find_one({"username": "geminerald"})
    my_lists = mongo.db.lists.find({"list_username": "geminerald"})
    return render_template('profile.html', user=my_account, lists=my_lists, title='My Account')


"""
List Search function - Takes a buyer to their desiered wishlist for someone they want to buy for. 
"""
@app.route('/listsearch')
def list_search():
    user = request.form.get('search')
    the_list = mongo.db.lists.find_one({'phone_number': user})
    return redirect(url_for('view_wishlist', list_id=list_id))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
