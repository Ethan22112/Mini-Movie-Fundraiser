import pandas as pd

#lists to store ticket details

all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_ticket_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket_Price': all_ticket_costs,
    'Ticket_Surcharge': all_ticket_surcharges
}

#create data frame / table from dictionary

mini_movie_frame = pd.DataFrame(mini_movie_dict)

print(mini_movie_frame)
