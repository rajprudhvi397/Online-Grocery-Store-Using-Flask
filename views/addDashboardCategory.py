from flask import Blueprint, jsonify, make_response,render_template, request # Importing Blueprint to handle routes related to addDashboardCategory page
import uuid # Importing module to generate random id's for the categories
from .makeURLName import makeURLName # Importing makeURLName function to make url compatible name for given entries
from .import db # Importing db to from __init__.py to work with database
from .models import Category # Importing Category from models.py to add data in this table

addDashboardCategory = Blueprint('addDashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@addDashboardCategory.route('/',methods=['POST'])
def renderAddDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''

    req = request.get_json() # Getting the request
    categoryName = req['category-name'] # Getting the category name
    print(categoryName)
    categoryId = str(uuid.uuid1()) # Generating a ranom Id of the category
    categoryURLName = makeURLName(categoryName) # Getting a url compatible name for the category

    categoryObject = Category(categoryId=categoryId,categoryName=categoryName,categoryURLName=categoryURLName) # Making an object to add in database

    responseData = {}

    # Handling Error
    try:
        db.session.add(categoryObject) # Adding to database
        db.session.commit() # Commiting to database
        # Making a dictionary to gather response data
        responseData = {
            'categoryName': categoryName,
            'categoryId': categoryId,
            'categoryURLName': categoryURLName
        }

        responseJson = make_response(jsonify(responseData),200) # Making a JSON response with status code 200
        return responseJson # Returning response

    except Exception as e:
        print(e)
        responseData = {
            'error': e
        }

        responseJson = make_response(jsonify(responseData),500) # Making a JSON response with status code 500 which means there is some error in server
        return responseJson # Returning response