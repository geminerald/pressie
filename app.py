from forms import RegistrationForm, LoginForm
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/finder')
def finder():
    return render_template('finder.html', title='Find a Wishlist')


@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html', title='Create a Wishlist')


@app.route('/additems')
def additems():
    return render_template('additems.html', title='Add Items to your Wishlist')


@app.route('/profile')
def profile():
    return render_template('profile.html', title='My Account')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
