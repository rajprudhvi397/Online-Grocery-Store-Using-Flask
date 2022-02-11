from flask import Blueprint,render_template # Importing Blueprint to handle routes related to account page

account = Blueprint('account',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@account.route('/')
def renderAccountPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('account.html') # Rendering account.html page