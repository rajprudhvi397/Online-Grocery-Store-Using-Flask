'''
FILE DESCRIPTION :- THIS FILE WILL HANDLE THE ROUTE RELATED TO THE CATEGORY OF THE WEBSITE
'''

from flask import Blueprint,render_template # Importing Blueprint to handle routes related to category page

category = Blueprint('category',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@category.route('/<categoryId>')
def renderCategoryPage(categoryId):
    ''' This is the function that will run when someone called for '/category' route '''
    return render_template('category.html') # Rendering category.html page