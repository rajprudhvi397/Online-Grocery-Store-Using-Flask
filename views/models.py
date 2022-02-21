""" FILE DESCRIPTION : THIS FILE WILL CREATE DATABASE MODELS NEEDED FOR THE WEBSITE """

from enum import unique
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

''' THROUGH THE FOLLOWING WAY WILL SET CART, ORDERS AND ORDER MODELS OF THE WEBSITE'''
'''
The Cart Model will contain cart items as rows and the model will contain 4 columns
The columns of the model will be as userId, productId, quantityId and itemId
All the rows conaining same userId means this rows are of same user means these items are in the corresponding users cart
When someone will buy this cart then all the rows containing userId will be deletd and this data will be replicated in orders model just changing Itemid by OrderId which will not be unique for each row and removing productId and productQuantity.
Same Order Id for different rows means the items corresponding to these rows are in same order.
Also there will be one more Model which would be Order having rows as userId, totalPrice, totalItems and OrderId
This orderId will be same as that in Orders column
'''

class Cart(db.Model):
    ''' This model will store all the items of cart of the website '''
    userId = db.Column(db.String(10000),nullable=False)
    productId = db.Column(db.String(10000),nullable=False)
    productQuantity = db.Column(db.Integer(1000),nullable=False)
    itemId = db.Column(db.String(10000),nullable=False,primary_key=True,unique=True)

class Orders(db.Model):
    ''' This model will store all the items of cart of the website '''
    userId = db.Column(db.String(10000),nullable=False)
    itemId = db.Column(db.String(10000),nullable=False,primary_key=True,unique=True)