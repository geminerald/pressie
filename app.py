import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'pressie'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser1@zwcluster1-znjzd.pressie.net/bugzap?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
