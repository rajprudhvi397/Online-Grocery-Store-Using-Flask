from flask import Blueprint,request,make_response,jsonify # Importing Blueprint to handle routes related to removeDashboardCategory page
from . import db # Importing database
from .models import Category # Importing Category from models.py

removeDashboardCategory = Blueprint('removeDashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@removeDashboardCategory.route('/',methods=['POST'])
def renderRemoveDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''

    req = request.get_json() # Getting Json Data
    categoryID = req['category-Id'] # Getting category id from request
    categoryObject = Category.query.filter_by(categoryId=categoryID).first() # Filtering the object having the id equal to the on ein json file


    try:
        db.session.delete(categoryObject)
        db.session.commit()
        
        responseData = {
            'status': 'ok'
        } # Creating response Data

        responseJson = make_response(jsonify(responseData),200) # Making a JSON response with status code 200
        return responseJson # Returning response

    except Exception as e:
        responseData = {
            'error': e
        } # Making a response data dictionary

        responseJson = make_response(jsonify(responseData),500) # Making a JSON response with status code 200
        print(e)