from flask import Blueprint,render_template, request, flash, redirect # Importing Blueprint to handle routes related to login page
from flask_login import current_user, login_user # Importing stuff needed to login user
# from . import db # Importing db from __init__.py to add data in server
from .models import User # Importing User Database Model from models.py to create Users for the website
from werkzeug.security import check_password_hash # Importing module to check wether the password and email are correct or not
from .checkEmail import checkEmail # Importing checkEmail Function from checkEmail.py to check if the email is valid or not

login = Blueprint('login',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@login.route('/',methods=['GET','POST'])
def renderLoginPage():
    ''' This is the function that will run when someone called for '/' route '''
    if request.method == 'POST':
        emailIdUser = request.form['email'] # Getting Email Id from Login form of the website
        passwordLogin = request.form['password'] # Getting Email Id from Login form of the website

        isEmailValid = checkEmail(emailIdUser) # Checking if email is a valid email or not

        # If email of User is correct
        if isEmailValid:
            userObject = User.query.filter_by(emailOfUser=emailIdUser).first() # This variable will return true if email exists

            if userObject:
                # Checking if user has typed correct password
                if check_password_hash(userObject.passwordOfUser,passwordLogin):
                    loginSuccessful =  login_user(userObject,remember=True) # Logging the user in
                    if loginSuccessful:
                        return redirect('/') # returning to home page
                    else:
                        flash("Something went wrong while logging the user in",category='error')
                        return redirect('/') # returning to home page

                else:
                    flash("Invalid Credentials",category='error')
                    return redirect('/') # returning to home page

            else:
                flash("Invalid Credentials",category='error')
                return redirect('/') # returning to home page
        
        else: # If user email isn't valid
            flash("Email is not Valid",category='error')
            return redirect('/') # returning to home page

    return render_template('login.html',title='Login - TB Grocery Store',user=current_user) # Rendering login.html page