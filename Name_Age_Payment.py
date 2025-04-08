def int_check(question, name):
    """Checks if user(s) enter an integer / float that is more than zero
       (or optional exit code)"""
    
    error = "Oops - please enter an integer"
    
    while True:
        try:
            #checks if response is an integer, returns value if so. 
            response = int(input(question))

            return response

        except ValueError: 
            #returns an error message if the response is not an integer
            print(error)


#main routine goes here

#loop for testing purposes
while True:
    print()

    #asks user their name

    name = input('Name: ')

    #Asks the user for their age, checking if it is between 12 and 120
    age = int_check('Age: ', name)
    
    if age < 12:
        print(f'{name} is too young')
        continue
    elif age > 120:
        print(f'{name} is too old')
        continue
    else:
        print(f'{name} has bought a ticket')
        continue


