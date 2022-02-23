from flask import Blueprint, redirect,render_template # Importing Blueprint to handle routes related to account page
from flask_login import current_user

account = Blueprint('account',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@account.route('/')
def renderAccountPage():
    ''' This is the function that will run when someone called for '/' route '''
    if current_user.is_authenticated:
        return render_template('account.html',title='Your Account - TB Grocery Store',user=current_user) # Rendering account.html page
    else:
        return redirect('/login') # Redirecting to login page if not logged in but still trying to access account page