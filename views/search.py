'''
FILE DESCRIPTION :- THIS FILE WILL HANDLE THE ROUTE RELATED TO THE SEARCH OF THE WEBSITE
'''

from flask import Blueprint,render_template # Importing Blueprint to handle routes related to search page

search = Blueprint('search',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@search.route('/')
def renderSearchPage():
    ''' This is the function that will run when someone called for '/search' route '''
    return render_template('search.html') # Rendering search.html page