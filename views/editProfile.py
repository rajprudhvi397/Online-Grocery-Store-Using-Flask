from flask import Blueprint,render_template,redirect,flash,request
from flask_login import current_user # Importing Blueprint to handle routes related to editProfile page
from .checkEmail import checkEmail
from werkzeug.security import generate_password_hash # Importing module to hash password of the user
from . import db
from .models import User

editProfile = Blueprint('editProfile',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editProfile.route('/',methods=['GET','POST'])
def renderEditProfilePage():
    ''' This is the function that will run when someone called for '/' route '''

    if request.method == 'POST':
        realNameOfUser = request.form['name'] # Getting the real Name of User
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

        isEmailValid = checkEmail(emailId) # Checking if email is valid or not

        if isEmailValid:

            doesEmailExists = User.query.filter_by(emailOfUser=emailId).first() # This variable will return true if email exists

            if doesEmailExists:
                flash("This email already exists, Please Login to access your account",category='error')
                return redirect('/editProfile') # returning to signup page

            userObject = User.query.filter_by(userId=current_user.userId).first() # Getting user object of current user
            # Filling through User Table
            userObject.realNameOfUser = realNameOfUser
            userObject.emailOfUser = emailId
            userObject.houseNumber = houseNumber
            userObject.residenceName = residenceName
            userObject.cityName = cityName
            userObject.pincode = pincode
            userObject.stateName = state
            userObject.countryName = country
            userObject.mobileNumber = mobileNumber


            if password == confirmPassword:
                
                if len(password) == 0:
                    pass

                elif len(password) >= 5:
                    userObject.passwordOfUser = generate_password_hash(password)

                else:
                    flash("Password must be atleast of 5 characters",category='error')
                    return redirect('/editProfile') # returning to edit profile page

                try:
                    db.session.add(userObject)
                    db.session.commit()
                    flash('Profile Successfully Edited', category='success')
                    return redirect('/account') # returning to accounts page
                except Exception as e:
                    flash(f'Some Error Occured while editing the profile, your profile may not have been changed {e}', category='error')
                    return redirect('/editProfile') # returning to edit profile page

            else:
                flash("Both Passwords are not same",category='error')
                return redirect('/editProfile') # returning to edit profile page
        
        else:
            flash("The given email isn't valid",category='error')
            return redirect('/editProfile') # returning to edit profile page

    return render_template('editProfile.html',title='Edit your profile - TB Grocery Store',user=current_user) # Rendering editProfile.html page