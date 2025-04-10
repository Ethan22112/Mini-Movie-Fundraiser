#Functions Go Above Main Routine

#this function checks if the age that the user(s) entered is an integer, displays an error message if it isn't 
def int_check(question):

    #continuously executes the chunk of code that is below the while loop unless a value has been returned, or a 'break' code was executed

    while True:
         try:

           #asks the user(s) for their age
           age = int(input(question))
           return age

         except ValueError:
            #displays error message if variable (age) is empty
            print("Please enter an integer")

#This function checks if the user(s) have not entered a blank name
def not_blank(question):

    # continuously executes the code below the while loop unless a value has been returned, or if a 'break' code was executed
    while True:

        name = input(question)
        #checks if variable 'name' is not empty, returns the value that is in variable 'name' if so.
        if name != "":
            return name
        else:
            #displays error message if variable 'name' is empty
            print("Sorry, this can't be blank, please try again")
            print()

#this function lets the user(s) choose between 'cash' or 'credit', or the first few numbers of each option according to variable 'num_letters' 
def string_check(question, payment_ans = ('cash', 'credit'), num_letters = 1):

    # the role of this variable is to check if the while loop below has returned any values
    Return = False

    #the while loop executes the code within it continuously until a value has been returned, or a 'break' code has been executed
    while True:
         #asks the user(s) for their name
         response = input(question).lower()
         #goes over each value in array 'payment_ans' checks if variable 'response' matches with any of them
         if response in payment_ans:
            #returns the value that is in variable 'response' 
            return response
         else:
            #checks if only the first two, or the value that is in variable 'num_letters' matches with the first two, or the value that is in 'num_letters' of the current value in 'payment_ans' 
            for item in payment_ans:
                if response == item[:num_letters]:

                    '''sets variable 'return' to True as the value in variable 'response' matches with one of the values in 'payment_ans' this 
                    prevents the program from displaying an error message'''

                    Return = True
                    if response == 'ca':
                        return 'cash'
                    elif response == 'cr':
                        return "credit"
            #executes this 'if' statement if boolean 'Return' remains False
            if Return == False:
              print(f"Please choose an option from {payment_ans}")

#Main Routine Goes Here

# initialize variables / non-default options for string_checker
payment_ans = ('cash', 'credit')

#loop for tesing purposes
while True:
    print()

    #asks the user(s) for their name, and checks that it is not blank
    name = not_blank("Name: ")

    #asks the user(s) for their age, and checks if it is between the minium age (12) and the maximum age (120)
    age = int_check("Age: ")

    #Output Error Message / Success Message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    #asks the user for their payment method (cash / credit or the first two letters of each option)
    pay_method = string_check("Payment Method: ", payment_ans = ('cash', 'credit'), num_letters = 2)
    print(f'{name} has bought a ticket ({pay_method})')
