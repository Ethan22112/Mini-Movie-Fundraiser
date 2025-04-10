#Functions Go Above Main Routine
def int_check(question):

    while True:
         try:

           age = int(input(question))
           return age

         except ValueError:
            print("Please enter an integer")


def not_blank(question):

    name = input(question).lower()

    while True:
        if name != "":
            return name
        else:
            print("Please enter a name")


def string_check(question, payment_ans = ('cash', 'credit'), num_letters = 1):

    Return = False
    
    while True:
         response = input(question).lower()
         if response in payment_ans:
            return response
         else:
            for item in payment_ans:
                if response == item[:num_letters]:
                    Return = True
                    return response
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
