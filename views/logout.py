from flask import Blueprint, flash, redirect # Importing Blueprint to handle routes related to logout page
from flask_login import current_user, logout_user

logout = Blueprint('logout',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@logout.route('/')
def renderLogoutPage():
    ''' This is the function that will run when someone called for '/' route '''
    if current_user.is_authenticated:
        try:
            logout_user()
            return redirect('/') # Redirecting to home page
        
        except:
            flash('Some Error Occured while logging out',category='error')
            return redirect('/') # Redirecting to home page
        
    else:
        return redirect('/login') # Redirecting to login page if not logged in but still trying to access logout page