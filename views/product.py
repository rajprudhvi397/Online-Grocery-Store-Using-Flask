'''
FILE DESCRIPTION :- THIS FILE WILL HANDLE THE ROUTE RELATED TO THE PRODUCT OF THE WEBSITE
'''

from flask import Blueprint,render_template # Importing Blueprint to handle routes related to product page

product = Blueprint('product',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@product.route('/<productId>')
def renderproductPage(productId):
    ''' This is the function that will run when someone called for '/product' route '''
    return render_template('product.html') # Rendering product.html page