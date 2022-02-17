from flask import Blueprint,render_template # Importing Blueprint to handle routes related to checkout page

checkout = Blueprint('checkout',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@checkout.route('/')
def renderCheckoutPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('checkout.html') # Rendering checkout.html page