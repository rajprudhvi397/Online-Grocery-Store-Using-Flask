from flask import Blueprint,render_template # Importing Blueprint to handle routes related to dashboardCategory page

dashboardCategory = Blueprint('dashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@dashboardCategory.route('/')
def renderDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('dashboardCategory.html') # Rendering dashboardCategory.html page