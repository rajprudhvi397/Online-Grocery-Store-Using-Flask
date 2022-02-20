from flask import Blueprint,render_template # Importing Blueprint to handle routes related to addDashboardCategory page

addDashboardCategory = Blueprint('addDashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@addDashboardCategory.route('/')
def renderAddDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('addDashboardCategory.html') # Rendering addDashboardCategory.html page