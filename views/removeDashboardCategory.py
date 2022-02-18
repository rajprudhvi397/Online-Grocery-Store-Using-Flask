from flask import Blueprint,render_template # Importing Blueprint to handle routes related to removeDashboardCategory page

removeDashboardCategory = Blueprint('removeDashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@removeDashboardCategory.route('/')
def renderRemoveDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('removeDashboardCategory.html') # Rendering removeDashboardCategory.html page