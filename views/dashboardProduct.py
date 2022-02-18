from flask import Blueprint,render_template # Importing Blueprint to handle routes related to dashboardProduct page

dashboardProduct = Blueprint('dashboardProduct',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@dashboardProduct.route('/')
def renderdashboardProductPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('dashboardProduct.html') # Rendering dashboardProduct.html page