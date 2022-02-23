import re

def checkEmail(email):
    ''' This Function will check wether the email given by the user and return true or false according to that '''
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # Creating Regex Varaible to create a skeleton of an ideal email so that if email given by the user is out of its domain the it will find it out

    if re.search(regex,email):
        return True  # Returning True to show that email is valid
    else:   
        return False # Returning False to show that email is invalid