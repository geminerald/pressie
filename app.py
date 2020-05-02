import os
from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, redirect, request, url_for, flash
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

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

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
        users.insert_one({"username": form.username.data,"email":form.email.data,"password":pw_hash,"admin":False})
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home',loggedin = True, username = username))
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pressie.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home',loggedin = True))
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
    return redirect(url_for('additems'))


@app.route('/delete_wishlist/<list_id>')
def delete_wishlist(list_id):
    mongo.db.lists.remove({'_id': ObjectId(list_id)})
    return redirect(url_for('profile'))


@app.route('/additems')
def additems():

    return render_template('additems.html', title='Add Items to your Wishlist')


@app.route('/profile')
def profile():
    my_account = mongo.db.users.find_one({"username": "geminerald"})
    my_lists = mongo.db.lists.find({"list_username": "geminerald"})
    return render_template('profile.html',user=my_account, lists=my_lists, title='My Account')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
