def makeURLName(name):
    ''' This function will take a name and it will generate a url compatible name for the given name '''
    namePartList = [] # Creating a list for storing parts of given string
    name = name.lower()
    finalURLName = '' # This will be the final url name
    nameList = name.split(' ')

    for i in nameList:
        nameVar2 = ''

        for e in i:
            if e.isalnum():
                nameVar2 += e
        
        if nameVar2 != '':
            namePartList.append(nameVar2)
    
    for i in namePartList:
        if namePartList.index(i) == len(namePartList)-1:
            finalURLName += f"{i}"
            break

        finalURLName += f"{i}-"
    
    return finalURLName # Returning final name for url