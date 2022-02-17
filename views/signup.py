from flask import Blueprint,render_template # Importing Blueprint to handle routes related to signup page

signup = Blueprint('signup',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@signup.route('/')
def renderSignupPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('signup.html') # Rendering signup.html page