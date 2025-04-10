def int_check(question, name):
    """Asks the user(s) for their name and their age, and checks if their age is between 12 and 120"""
    
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

MINIMUM_AGE = 12
MAXIMUM_AGE = 120

while True:
    print()

    #asks user their name

    name = input('Name: ')

    #Asks the user for their age, checking if it is between 12 and 120
    age = int_check('Age: ', name)
    
    if age < MINIMUM_AGE:
        print(f'{name} is too young')
        continue
    elif age > MAXIMUM_AGE:
        print(f'{name} is too old')
        continue
    else:
        print(f'{name} has bought a ticket')
        continue


