from flask import Blueprint,render_template # Importing Blueprint to handle routes related to editDashboardDetails page

editDashboardDetails = Blueprint('editDashboardDetails',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editDashboardDetails.route('/')
def renderEditDashboardDetailsPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('editDashboardDetails.html') # Rendering editDashboardDetails.html page