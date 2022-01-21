from flask import Blueprint,render_template # Importing Blueprint to handle routes related to home page

home = Blueprint('home',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@home.route('/')
def renderHomePage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('home.html') # Rendering home.html page