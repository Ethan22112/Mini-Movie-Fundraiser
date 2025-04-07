#functions go above main routine
def make_statement(question, decoration):
    #statement function, prints decoration 3 times before printing the statement, before printing the decoration three more times
    print()
    print(f'{decoration * 3} {question} {decoration * 3}')

def string_Check(question, valid_answers = ("yes", "no"), num_letters = 1):
    #String checker
    Error_Code = 'xxx'
    response = input(question).lower()

    if(response in valid_answers):
        return response
    else:
        print(f"Please Choose An Option From {valid_answers}")


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

#main routine goes here
make_statement("Mini_Movie Fundraiser Program", '🎞️')

print()
want_instructions = string_Check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program Continues")