import os
from forms import RegistrationForm, LoginForm, CreateWishlist
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
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
sqla = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user)


class User(sqla.Model, UserMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    username = sqla.Column(sqla.String(20), unique=True, nullable=False)
    email = sqla.Column(sqla.String(120), unique=True, nullable=False)
    password = sqla.Column(sqla.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        users = mongo.db.users
        users.insert_one({"username": username,
                          "email": form.email.data, "password": pw_hash, "admin": False})
        flash(f'Account Created for {username}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = mongo.db.users.find_one({'email': email})
        if user:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check email and password', 'danger')
    return render_template('login.html', title='Sign In', form=form)





@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/finder')
def finder():
    return render_template('finder.html', title='Find a Wishlist')


@app.route('/wishlist')
def wishlist():
    users = mongo.db.users.find()
    return render_template('wishlist.html', title='Create a Wishlist', users=users)


@app.route('/insert_wishlist', methods=['GET', 'POST'])
def insert_wishlist():
    lists = mongo.db.lists
    lists.insert_one(request.form.to_dict())
    return redirect(url_for('profile'))


@app.route('/view_wishlist/<list_id>')
def view_wishlist(list_id):
    myquery = {"list_id": list_id}
    items = mongo.db.items.find(myquery)
    pass_in_list_id = list_id
    return render_template('view_wishlist.html', items=items, list_id=pass_in_list_id)


@app.route('/delete_wishlist/<list_id>')
def delete_wishlist(list_id):
    mongo.db.lists.remove({'_id': ObjectId(list_id)})
    return redirect(url_for('profile'))


@app.route('/additems/<list_id>')
def additems(list_id):
    the_list = mongo.db.lists.find_one({"_id": ObjectId(list_id)})
    the_list_id = the_list['_id']
    items = mongo.db.items
    return render_template('additems.html', title='Add Items to your Wishlist', item_list_id=the_list_id)


@app.route('/insert_items', methods=['GET', 'POST'])
def insert_items():
    items = mongo.db.items
    items.insert_one(request.form.to_dict())
    return redirect('profile')


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    the_item = mongo.db.items
    the_list = the_item.list_id
    the_item.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('view_wishlist', list_id=the_list))


@app.route('/profile')
def profile():
    my_account = mongo.db.users.find_one({"username": "geminerald"})
    my_lists = mongo.db.lists.find({"list_username": "geminerald"})
    return render_template('profile.html', user=my_account, lists=my_lists, title='My Account')


@app.route('/list_search')
def list_search():
    user = request.form.get('search')
    the_list = mongo.db.lists.find_one({'phone_number': user})
    return redirect(url_for('view_wishlist', list_id=list_id))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
