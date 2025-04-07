#Initializing the ticket variables, note that MAX_TICKETS is in all uppercase as it is a constant
MAX_TICKETS = 5
Tickets_Sold = 0

#continues executing the code below the while loop, while Variable Tickets_Sold
while Tickets_Sold <= MAX_TICKETS:
    #Initializing Error Code
    Error_Code = 'xxx'
    name = input("Please Enter Your Name: ")

    #Checks if Variable Name equals to the Error Code
    if(name == Error_Code):
        break

    #adds Variable Tickets_Sold by one every time a name is inputted
    Tickets_Sold += 1

#Checks Whether the amount of 'Tickets_Sold' has exceeded, or matched the value in MAX_TICKETS
if Tickets_Sold >= MAX_TICKETS:
    print(f'You have sold all of the tickets, you have {Tickets_Sold} / {MAX_TICKETS} tickets sold')
else:
    print(f'You have sold {Tickets_Sold} / {MAX_TICKETS} tickets')
