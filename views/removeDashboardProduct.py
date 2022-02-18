from flask import Blueprint,render_template # Importing Blueprint to handle routes related to removeDashboardProduct page

removeDashboardProduct = Blueprint('removeDashboardProduct',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@removeDashboardProduct.route('/')
def renderRemoveDashboardProductPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('removeDashboardProduct.html') # Rendering removeDashboardProduct.html page