from flask import Blueprint,render_template # Importing Blueprint to handle routes related to login page

login = Blueprint('login',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@login.route('/')
def renderLoginPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('login.html') # Rendering login.html page