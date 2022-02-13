from flask import Blueprint,render_template # Importing Blueprint to handle routes related to cart page

cart = Blueprint('cart',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@cart.route('/')
def renderCartPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('cart.html') # Rendering cart.html page