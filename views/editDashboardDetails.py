from flask import Blueprint,render_template, redirect,request,flash
from flask_login import current_user
from werkzeug.security import generate_password_hash # Importing module to hash password of the user
from views.checkEmail import checkEmail # Importing Blueprint to handle routes related to editDashboardDetails page
from . import db
from .models import User

editDashboardDetails = Blueprint('editDashboardDetails',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@editDashboardDetails.route('/',methods=['GET','POST'])
def renderEditDashboardDetailsPage():
    ''' This is the function that will run when someone called for '/' route '''

    if current_user.is_authenticated:
        if current_user.userId == 'owner':

            if request.method == 'POST':
                newEmailId = request.form['email']
                newPassword = request.form['password']
                confirmPassword = request.form['confirm-password']
                isEmailValid = checkEmail(newEmailId) # Checking if email is valid or not

                if isEmailValid:
                    
                    if newPassword == confirmPassword:

                        userObject = User.query.filter_by(userId='owner').first() # Getting user object of owner
                        userObject.emailOfUser = newEmailId
                        
                        if len(newPassword) == 0:
                            pass

                        elif len(newPassword) >= 5:
                            userObject.passwordOfUser = generate_password_hash(newPassword)

                        else:
                            flash("Password must be atleast of 5 characters",category='error')
                            return redirect('/dashboard/editDashboardDetails') # returning to same page
                        
                        try:
                            db.session.add(userObject)
                            db.session.commit()
                            flash('Profile Successfully Edited', category='success')
                            return redirect(f'/dashboard') # Redirecting to the dashboard page
                        except:
                            flash('Some Error Occured while editing the profile, your profile may not have been changed', category='error')
                            return redirect(f'/dashboard/editDashboardDetails') # Redirecting to the same profile

                    else:
                        flash("Both Passwords are not same",category='error')
                        return redirect('/dashboard/editDashboardDetails') # returning to same page

                else:
                    flash("The given email isn't valid",category='error')
                    return redirect('/dashboard/editDashboardDetails') # returning to same page

            return render_template('editDashboardDetails.html',title='Edit Details related to Dashboard here',user=current_user) # Rendering editDashboardDetails.html page
        else:
            return redirect('/') # Redirecting a non owner to home page
    else:
        return redirect('/login') # Redirecting to Login page