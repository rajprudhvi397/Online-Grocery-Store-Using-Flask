''' Project Name : TB Grocery Store '''
''' Project Description : This is a website that is made for a grocery store and is having all the
features neeeded for the store to grow. '''
''' Author : Harshu Prasad Shukla '''

''' FILE DESCRIPTION : THIS IS THE MAIN FILE THAT RUNS THE PROJECT '''

from views import createApp # Importing createApp from __init__.py file in views directory

app = createApp() # Creating app using function createApp from __init__.py file in views directory

if __name__ == '__main__':
    app.run(debug=True,port=5001) # Runs Server at port 5001