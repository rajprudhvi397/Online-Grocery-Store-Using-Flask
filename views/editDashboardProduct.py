from flask import Blueprint,render_template # Importing Blueprint to handle routes related to editDashboardProduct page

editDashboardProduct = Blueprint('editDashboardProduct',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editDashboardProduct.route('/')
def renderEditDashboardProductPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('editDashboardProduct.html') # Rendering editDashboardProduct.html page