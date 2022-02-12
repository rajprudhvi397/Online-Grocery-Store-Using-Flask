'''
FILE DESCRIPTION : THIS IS A VERY IMPORTANT FILE THAT WILL CREATE DATABASE, CONNECT TO DATABASE,
REGISTER BLUEPRINTS AND MUCH MORE WHICH IS A CRUCIAL PART TO MAKE THE WEBSITE
'''

# from math import prod
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path # Importing Path from os module to check path of database
# from flask_login import LoginManager # Importing Class LoginManager to manage Login Details

db = SQLAlchemy() # Creating Database Instance
DATABASENAME = 'database.db' # This is the name of the database that the website will be using

def createApp():
    ''' This function will create the app '''
    app = Flask(__name__) # Initializing Flask Module
    app.config['SECRET_KEY'] = 'sjdflksajflksajfsajflksajl' # Setting up the secret key for the application
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ADD This line to remove warnings
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASENAME}'
    db.init_app(app) # Adding App in Database

    from .home import home # Importing home from home.py which will help us to adress the '/' route of the website

    from .category import category

    from .product import product

    from .account import account

    app.register_blueprint(home,url_prefix='/') # Registering Blueprint so that all '/' requests are redirected to code of home.py

    app.register_blueprint(category,url_prefix='/category') # Register blueprint to access /category route of the website

    app.register_blueprint(product,url_prefix='/product') # Register blueprint to access /product route of the website

    app.register_blueprint(account,url_prefix='/account') # Register blueprint to access /account route of the website 

    createDatabase(app) # Running createDatabase function to create database if it doesn't exists

    return app # Returning App so that it could run in main.py

def createDatabase(app):
    ''' This function will create database for the website '''
    if not path.exists('views/' + DATABASENAME): # If database doesn't exists
        db.create_all(app=app) # Creating Database
        print('Created Database!')