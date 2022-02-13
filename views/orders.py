from flask import Blueprint,render_template # Importing Blueprint to handle routes related to orders page

orders = Blueprint('orders',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@orders.route('/')
def renderOrdersPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('orders.html') # Rendering orders.html page