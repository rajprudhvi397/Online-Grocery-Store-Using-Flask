from flask import Blueprint,render_template
from flask_login import current_user # Importing Blueprint to handle routes related to editDashboardProduct page

editDashboardProduct = Blueprint('editDashboardProduct',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editDashboardProduct.route('/<productId>')
def renderEditDashboardProductPage(productId):
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('editDashboardProduct.html',title='Edit Product Details - TB Grocery Store',user=current_user) # Rendering editDashboardProduct.html page