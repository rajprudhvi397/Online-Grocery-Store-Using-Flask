from flask import Blueprint,render_template # Importing Blueprint to handle routes related to viewOrder page

viewOrder = Blueprint('viewOrder',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@viewOrder.route('/<orderId>')
def renderViewOrderPage(orderId):
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('viewOrder.html') # Rendering viewOrder.html page