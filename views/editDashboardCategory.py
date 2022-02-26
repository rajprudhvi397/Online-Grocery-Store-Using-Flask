from flask import Blueprint,render_template,request,make_response,jsonify # Importing Blueprint to handle routes related to editDashboardCategory page
from flask_login import current_user # Importing neccessary items from flask_login to do stuff related to login
from .models import Category
from .import db

editDashboardCategory = Blueprint('editDashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editDashboardCategory.route('/',methods=['POST'])
def renderEditDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''
    # Category.query.delete()

    # db.session.query(Category).delete()
    # db.session.commit()

    req = request.get_json() # Getting Json Data
    categoryName = req['new-category-name'] # Getting the new category name
    categoryId = req['categoryId'] # Getting the new category name
    categoryObject = Category.query.filter_by(categoryId=categoryId).first() # Getting category having this category id
    categoryObject.categoryName = categoryName # Setting new category name

    try:
        db.session.add(categoryObject) # Adding to the database
        db.session.commit() # Commiting to the database
        responseData = {
            'status': 'ok'
        } # Making a response data dictionary

        responseJson = make_response(jsonify(responseData),200) # Making a JSON response with status code 200
        return responseJson # Returning response

    except Exception as e:
        responseData = {
            'error': e
        } # Making a response data dictionary

        responseJson = make_response(jsonify(responseData),500) # Making a JSON response with status code 200
        return responseJson # Returning response