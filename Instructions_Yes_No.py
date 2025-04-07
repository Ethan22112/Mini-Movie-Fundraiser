# Functions Go Here
def yes_no(question):
    """Checks that users enters a yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return "Yes"
        elif response == 'no' or response == 'n':
            return "No"
        else:
            print('Please enter yes (y) or no (n).\n')

# Main Routine Goes Here
while True:
  Read_Instructions = yes_no('Do You Want To Read The Instructions? ')
  print(f'You chose {Read_Instructions}\n')