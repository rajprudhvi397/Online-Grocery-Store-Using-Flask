from flask import Blueprint,render_template # Importing Blueprint to handle routes related to editProfile page

editProfile = Blueprint('editProfile',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editProfile.route('/')
def renderEditProfilePage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('editProfile.html') # Rendering editProfile.html page