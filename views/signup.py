from flask import Blueprint,render_template,request,redirect,flash # Importing Blueprint to handle routes related to signup page
from flask_login import current_user, login_user # Importing stuff needed to login user
from .checkEmail import checkEmail # Importing function to check if given email is a valid email
import uuid # Importing built in module uuid for generating random Id's
from . import db # Importing db from main.py to add data in server
from .models import User # Importing User Database Model from models.py to create Users for the website
from werkzeug.security import generate_password_hash # Importing module to hash password of the user

signup = Blueprint('signup',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@signup.route('/',methods=['GET','POST'])
def renderSignupPage():
    ''' This is the function that will run when someone called for '/' route '''
    if request.method == 'POST':
        realNameOfUser = request.form['name'] # Getting the real Name of User
        userName = str(uuid.uuid1()) # Generating a random Id for the user
        emailId = request.form['email'] # Getting the email of User
        password = request.form['password'] # Getting the password of User
        confirmPassword = request.form['confirm-password'] # Getting the confirmed password of User
        houseNumber = request.form['house-number'] # Getting the house number of User
        residenceName = request.form['residence-name'] # Getting the residence name of User
        cityName = request.form['city-name'] # Getting the city name of User
        pincode = request.form['pincode'] # Getting the pincode of User
        state = request.form['state'] # Getting the state of User
        country = request.form['country'] # Getting the country of User
        mobileNumber = request.form['mobile-number'] # Getting the mobile number of User

        if password == confirmPassword:
            isEmailValid = checkEmail(emailId) # Checking if Email is valid or not

            if isEmailValid:

                if len(password) < 5:
                    flash("Password must be atleast of 5 characters",category='error')
                    return redirect('/signup') # returning to signup page

                doesEmailExists = User.query.filter_by(emailOfUser=emailId).first() # This variable will return true if email exists

                if not doesEmailExists: # Means there is no user having same email then
                    newUser = User(userId=userName,realNameOfUser=realNameOfUser,emailOfUser=emailId,passwordOfUser=generate_password_hash(password),houseNumber=houseNumber,residenceName=residenceName,cityName=cityName,pincode=pincode,stateName=state,countryName=country,mobileNumber=mobileNumber)
                    # Filling all the important credentials to make a new User

                    # Checking wether the following Code would run or not
                    try:
                        db.session.add(newUser) # Adding Users to Database
                        db.session.commit() # Commiting Data to the Database
                        login_user(newUser) # Logging in User who has created the account
                        return redirect('/') # returning to home page

                    except:
                        flash("Some Error Occured while creating your account",category='error')
                        return redirect('/signup') # returning to signup page

                else:
                    flash("This email already exists, Please Login to access your account",category='error')
                    return redirect('/signup') # returning to signup page

            else:
                flash("The given email isn't valid",category='error')
                return redirect('/signup') # returning to signup page

        else:
            flash("Both the passwords don't match",category='error')
            return redirect('/signup') # returning to signup page

    return render_template('signup.html',title='Signup - TB Grocery Store',user=current_user) # Rendering signup.html page