from turtle import title
from flask import Blueprint, redirect,render_template # Importing Blueprint to handle routes related to dashboard page
from flask_login import current_user # Importing current_user to get loggin details

dashboard = Blueprint('dashboard',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@dashboard.route('/')
def renderDashboardPage():
    ''' This is the function that will run when someone called for '/' route '''
    if current_user.is_authenticated:
        if current_user.userId == 'owner':
            return render_template('dashboard.html',title='Shop Dashboard - TB Grocery Store',user=current_user) # Rendering dashboard.html page
        else:
            return redirect('/') 
    else:
        return redirect('/login') # Redirecting to Login page