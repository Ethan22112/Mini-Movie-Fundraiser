def string_check(question, valid_ans_list = ('yes', 'no'), num_letters = 1):
    """Checks if the users enter the full word, or the 'n' letters of a word
    from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item
            
            elif response == item[:num_letters]:
                return item
            
        print(f'please choose an option from {valid_ans_list}')

#Main Routine Goes Here
payment_list = ('cash', 'credit')

want_instructions = string_check('See Instructions? ')
print(f'you chose {want_instructions}')
pay_method = string_check('Payment method: ', payment_list, num_letters=2)
print(f'you chose {pay_method}')