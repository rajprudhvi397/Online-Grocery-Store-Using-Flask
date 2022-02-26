'''
FILE DESCRIPTION : THIS IS A VERY IMPORTANT FILE THAT WILL CREATE DATABASE, CONNECT TO DATABASE,
REGISTER BLUEPRINTS AND MUCH MORE WHICH IS A CRUCIAL PART TO MAKE THE WEBSITE
'''

# from math import prod
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path # Importing Path from os module to check path of database
from flask_login import LoginManager # Importing Class LoginManager to manage Login Details

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

    from .orders import orders

    from .viewOrder import viewOrder

    from .cart import cart

    from .editProfile import editProfile

    from .checkout import checkout

    from .login import login

    from .signup import signup

    from .dashboard import dashboard

    from .editDashboardDetails import editDashboardDetails

    from .dashboardCategory import dashboardCategory

    from .addDashboardCategory import addDashboardCategory

    from .dashboardProduct import dashboardProduct

    from .editDashboardProduct import editDashboardProduct

    from .addDashboardProduct import addDashboardProduct

    from .editDashboardCategory import editDashboardCategory

    from .removeDashboardCategory import removeDashboardCategory

    from .search import search

    from .logout import logout

    app.register_blueprint(home,url_prefix='/') # Registering Blueprint so that all '/' requests are redirected to code of home.py

    app.register_blueprint(category,url_prefix='/category') # Register blueprint to access /category route of the website

    app.register_blueprint(product,url_prefix='/product') # Register blueprint to access /product route of the website

    app.register_blueprint(account,url_prefix='/account') # Register blueprint to access /account route of the website 

    app.register_blueprint(orders,url_prefix='/orders') # Register blueprint to access /orders route of the website

    app.register_blueprint(viewOrder,url_prefix='/viewOrder') # Register blueprint to access /viewOrder route of the website 

    app.register_blueprint(cart,url_prefix='/cart') # Register blueprint to access /cart route of the website

    app.register_blueprint(editProfile,url_prefix='/editProfile') # Register blueprint to access /editProfile route of the website

    app.register_blueprint(checkout,url_prefix='/checkout') # Register blueprint to access /checkout route of the website

    app.register_blueprint(login,url_prefix='/login') # Register blueprint to access /login route of the website

    app.register_blueprint(logout,url_prefix='/logout') # Register blueprint to access /logout route of the website
    
    app.register_blueprint(signup,url_prefix='/signup') # Register blueprint to access /signup route of the website

    app.register_blueprint(dashboard,url_prefix='/dashboard') # Register blueprint to access /dashboard route of the website

    app.register_blueprint(dashboardCategory,url_prefix='/dashboard/dashboardCategory') # Register blueprint to access /dashboard/dashboardCategory route of the website

    app.register_blueprint(addDashboardCategory,url_prefix='/dashboard/dashboardCategory/addDashboardCategory') # Register blueprint to access /dashboard/dashboardCategory/addDashboardCategory route of the website

    app.register_blueprint(editDashboardCategory,url_prefix='/dashboard/dashboardCategory/editDashboardCategory') # Register blueprint to access /dashboard/editDashboardCategory route of the website

    app.register_blueprint(removeDashboardCategory,url_prefix='/dashboard/dashboardCategory/removeDashboardCategory') # Register blueprint to access /dashboard/removeDashboardCategory route of the website

    app.register_blueprint(dashboardProduct,url_prefix='/dashboard/dashboardProduct') # Register blueprint to access /dashboard/dashboardProduct route of the website

    app.register_blueprint(editDashboardProduct,url_prefix='/dashboard/editDashboardProduct') # Register blueprint to access /dashboard/editDashboardProduct route of the website

    app.register_blueprint(editDashboardDetails,url_prefix='/dashboard/editDashboardDetails') # Register blueprint to access /dashboard/editDashboardDetails route of the website

    app.register_blueprint(addDashboardProduct,url_prefix='/dashboard/addDashboardProduct') # Register blueprint to access /dashboard/addDashboardProduct route of the website

    app.register_blueprint(search,url_prefix='/search') # Register blueprint to access /search route of the website    

    createDatabase(app) # Running createDatabase function to create database if it doesn't exists

    loginManagerVariable = LoginManager() # Initialising Login Manager
    loginManagerVariable.login_view = 'login.loginUser'
    loginManagerVariable.init_app(app)

    from .models import User # Importing User Class from models.py

    @loginManagerVariable.user_loader
    def loadUser(userName):
        return User.query.get(str(userName))

    return app # Returning App so that it could run in main.py

def createDatabase(app):
    ''' This function will create database for the website '''
    if not path.exists('views/' + DATABASENAME): # If database doesn't exists
        db.create_all(app=app) # Creating Database
        print('Created Database!')