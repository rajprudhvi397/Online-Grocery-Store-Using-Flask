from flask import Blueprint,render_template # Importing Blueprint to handle routes related to dashboard page

dashboard = Blueprint('dashboard',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@dashboard.route('/')
def renderDashboardPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('dashboard.html') # Rendering dashboard.html page