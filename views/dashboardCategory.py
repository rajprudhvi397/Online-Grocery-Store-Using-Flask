from flask import Blueprint,render_template # Importing Blueprint to handle routes related to dashboardCategory page
from flask_login import current_user # Importing neccessary items from flask_login to do stuff related to login
from .models import Category

dashboardCategory = Blueprint('dashboardCategory',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@dashboardCategory.route('/')
def renderDashboardCategoryPage():
    ''' This is the function that will run when someone called for '/' route '''
    # Category.query.delete()

    # db.session.query(Category).delete()
    # db.session.commit()

    return render_template('dashboardCategory.html',title='Dashboard Category - TB Grocery Store',user=current_user,categories=Category.query.all()) # Rendering dashboardCategory.html page