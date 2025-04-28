#functions go above main routine
def make_statement(question, decoration):
    #statement function, prints decoration 3 times before printing the statement, before printing the decoration three more times
    print()
    print(f'{decoration * 3} {question} {decoration * 3}')

def string_check_instructions(question, valid_answers = ("yes", "no"), num_letters = 1):
    #String checker
    Error_Code = 'xxx'
    response = input(question).lower()

    if(response in valid_answers):
        return response
    else:
        print(f"Please Choose An Option From {valid_answers}")

def string_check_payment_method(question, payment_ans = ("yes", "no"), num_letters = 1):
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

def instructions():
    #instructions 
    make_statement("Instructions", ' ℹ️ ' )

    print('''
For each ticket holder enter ...
          
- Their Name
- Their Age
- The Payment Method (Cash / Credit)
          
The program will record the ticket sale and calculate 
the ticket cost (and the profit).
          
Once you have sold all of the tickets, or entered the exit code ('xxx'), the program will
display the ticket sales information and write the data to a text file.
          
it wil also choose one lucky ticket holder who wins the draw (their ticket is free).
''')

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
#main routine goes here

#Initializing the ticket variables, note that MAX_TICKETS is in all uppercase as it is a constant
MAX_TICKETS = 5
Tickets_Sold = 0

# initialize variables / non-default options for string_checker
payment_ans = ('cash', 'credit')

make_statement("Mini_Movie Fundraiser Program", '🎞️')

print()
want_instructions = string_check_instructions("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
while Tickets_Sold < MAX_TICKETS:
    #Initializing Error Code
    Error_Code = 'xxx'

    #asks the user(s) for their name, and checks that it is not blank
    print()
    name = not_blank("Name: ")

    #Checks if Variable Name equals to the Error Code
    if(name == Error_Code):
        break

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
    pay_method = string_check_payment_method("Payment Method: ", payment_ans = ('cash', 'credit'), num_letters = 2)
    print(f'{name} has bought a ticket ({pay_method})')

    #adds Variable Tickets_Sold by one every time a name is inputted
    Tickets_Sold += 1

#Checks Whether the amount of 'Tickets_Sold' has exceeded, or matched the value in MAX_TICKETS
if Tickets_Sold == MAX_TICKETS:
    print(f'You have sold all of the tickets, you have {Tickets_Sold} / {MAX_TICKETS} tickets sold')
else:
    print(f'You have sold {Tickets_Sold} / {MAX_TICKETS} tickets')