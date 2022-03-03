""" FILE DESCRIPTION : THIS FILE WILL CREATE DATABASE MODELS NEEDED FOR THE WEBSITE """

from . import db # Importing db variable to create database models from __init__.py
from flask_login import UserMixin # Importing UserMixin from flask_login module for loggin in users

# Creating Users Model for database
class User(db.Model, UserMixin):
    ''' This Model will store users data in database '''
    # Adding Coloumns
    userId = db.Column(db.String(10000),primary_key=True,unique=True)
    realNameOfUser = db.Column(db.String(250),nullable=False)
    emailOfUser = db.Column(db.String(250),nullable=False,unique=True) #Adding unique=True to add only unique emails in database
    passwordOfUser = db.Column(db.String(1000),nullable=False)
    houseNumber = db.Column(db.String(1000),nullable=False)
    residenceName = db.Column(db.String(10000),nullable=False)
    cityName = db.Column(db.String(3000),nullable=False)
    pincode = db.Column(db.String(1000),nullable=False)
    stateName = db.Column(db.String(5000),nullable=False)
    countryName = db.Column(db.String(5000),nullable=False)
    mobileNumber = db.Column(db.String(50),nullable=False)

    def get_id(self):
        ''' This function will override the default properties of get_id under the User Class '''
        return (self.userId)

class Category(db.Model):
    ''' This model will store all the categories of the website '''
    categoryId = db.Column(db.String(10000),nullable=False,primary_key=True,unique=True)
    categoryName = db.Column(db.String(1000),nullable=False)
    categoryURLName = db.Column(db.String(1000),nullable=False)

class Product(db.Model):
    ''' This model will store all the products of the website '''
    productId = db.Column(db.String(10000),nullable=False,primary_key=True,unique=True)
    productName = db.Column(db.String(1000),nullable=False)
    productURLName = db.Column(db.String(1000),nullable=False)
    productImageName = db.Column(db.String(10000),nullable=False)
    productPrice = db.Column(db.String(100000),nullable=False)
    categoryId = db.Column(db.String(10000),nullable=False) # This will be the Id of the category of which the product is
    categoryName = db.Column(db.String(1000),nullable=False)
    categoryURLName = db.Column(db.String(1000),nullable=False)

class Cart(db.Model):
    ''' This model will store all the items of cart of the website '''
    userId = db.Column(db.String(10000),nullable=False)
    productId = db.Column(db.String(10000),nullable=False)
    productQuantity = db.Column(db.Integer,nullable=False)
    itemId = db.Column(db.String(10000),nullable=False,primary_key=True,unique=True)
    cartId = db.Column(db.String(10000),nullable=False) # This is the id of all cart in which products are there different Items may have same cartId and if so then it means these items are in same cart
    cartActive = db.Column(db.String(10),nullable=False) # This column will either take True or False. If True it means that cart has not been bought yet and if False it means user has bought the cart

class Order(db.Model):
    ''' This model will contain all the data related to a any order that user has made'''
    orderNumber = db.Column(db.Integer,nullable=False,unique=True,primary_key=True) # This is the number of the order
    userId = db.Column(db.String(10000),nullable=False) # This will be the Id of user who has made this order
    orderId = db.Column(db.String(10000),nullable=False,unique=True) # This will be a unique Id of the order
    cartId = db.Column(db.String(10000),nullable=False) # This is the id of the cart that has been bought to make this order happen
    paymentMethod = db.Column(db.String(100),nullable=False) # This will store the payment method
    date = db.Column(db.String(100),nullable=False) # This is the date at which order was placed

''' HOW THE MODEL WILL WORK '''
'''
There are 5 Models in which User,Category and Product Model will store info about respective things
and Cart Model will store userId to know who's cart is it, productId to now what is the product of one item with quantity to know how much is the product and cartId to identify unique Carts and cartActive to
know wether a cart is active or has been bought.
Once somebody buys a cart it becomes unactive and a new cart is assigned to the user
The 5th Model is Order Model which will store info about orders made in entire website. Order Model will
contain 5 Columns which are OrderNumber to know which order is it,userId to know who has made the order,
OrderId to know uniquely identify an order, cartId to know of which cart is this order which cart was
bought to make the order happen and finally date to know when was the order made.
Date will be in form dd-mm-yyyy
'''