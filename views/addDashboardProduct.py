from flask import Blueprint,render_template,request,flash,redirect # Importing Blueprint to handle routes related to addDashboardProduct page
from flask_login import current_user
from .models import Category,Product # Importing Category and product from models.py to get information about Category and products
import uuid
import os
from . import app,db,allow_file
from .makeURLName import makeURLName # Importing makeURLName function to make url compatible name for given entries
from werkzeug.utils import secure_filename

addDashboardProduct = Blueprint('addDashboardProduct',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@addDashboardProduct.route('/',methods=['GET','POST'])
def renderAddDashboardProductPage():
    ''' This is the function that will run when someone called for '/' route '''

    if current_user.is_authenticated and current_user.userId == 'owner':

        if request.method == 'POST':

            if 'profileImage' not in request.files:
                flash('No file part',category='error')
                return redirect(request.url)
            file = request.files['profileImage'] # Getting Profile Image
            if file.filename == '':
                flash('No image selected for uploading',category='error')
                return redirect(request.url)
            
            if file and allow_file(file.filename):
                productImageName = f'{uuid.uuid4().hex}_{secure_filename(file.filename)}' # Getting the hex value to keep it as filename of choosed file
                productId = str(uuid.uuid1()) # Getting string value of a uuid to use it as a product id
                productName = request.form['name'] # Getting product name
                productPrice = request.form['productPrice'] # Getting product price
                productURLName = makeURLName(productName) # Getting a url compatible name for the product
                categoryIdOfProduct = request.form['categoryIdOfProduct'] # Getting category Id of which the product is
                categoryObject = Category.query.filter_by(categoryId=categoryIdOfProduct).first() # Getting the category which's having the id as choosed in form
                categoryName = categoryObject.categoryName # Getting the name of the category
                categoryURLName = categoryObject.categoryURLName # Getting the url name of the category

                try:
                    # open('b',os.path.join(app.config['UPLOAD_FOLDER']), productImageName).close()
                    file.save(os.path.join(app.config['UPLOAD_FOLDER']), productImageName) # Saving given file
                    productObject = Product(productId=productId,productName=productName,productURLName=productURLName,productImageName=productImageName,productPrice=productPrice,categoryId=categoryIdOfProduct,categoryName=categoryName,categoryURLName=categoryURLName) # Filling object to add it to database
                    db.session.add(productObject) # Adding it to the database
                    db.session.commit() # Commiting to database
                    return redirect('/dashboard')
                except Exception as e:
                    flash(f'Some Error {e}',category='error')
                    return redirect(request.url) # Redirecting to the same page as
            else:
                flash('Only files with extention jpg,jpeg and png are allowed',category='error')
                return redirect(request.url)

        return render_template('addDashboardProduct.html',title='Add Product - TB Grocery Store',user=current_user,categories=Category.query.all()) # Rendering addDashboardProduct.html page