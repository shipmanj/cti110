# A simple travel expense calculator
# 10-10-2022
# CTI-110 P2HW1-Travel
# JC Shipman
#

# Travel input prompts. Does not accept decimal places, only whole numbers.
print ('___________________________________________________________________') # A line.
print ('This program calculates and displays travel expenses.') #Display Program purpose
travel_budget = int(input('Enter Travel Budget:')) #Prompt for initial travel budget.
travel_destination = input('Please enter travel destination:') #Prompt for travel destination.
travel_gas = int(input('How much do you think you will spend on gas?:')) #Prompt for estimated gas expense.
travel_hotel = int(input('How much do you think accomodations will cost?:')) #Prompt for estimated accomodaton/hotel expense.
travel_food = int(input('How much will you need for food?:')) #Prompt for estimated food expense.

# Background Calculations
travel_cost = travel_gas + travel_hotel + travel_food #Adds the total estimate cost of gas, accomodations, and food.
travel_balance = travel_budget - travel_cost #Subtracts the estimated travel cost from the initial travel budget.


# Results
print ('------------Travel Expenses------------') #Travel Expense Line.
print(f'Location:           {travel_destination}') #Displays the travel destination.
print(f'Initial Budget:     ${travel_budget:.2f}') #Displays the initial travel budget.
print(f'Fuel:               ${travel_gas:.2f}') #Displays the estimated fuel cost.
print(f'Accomodation:       ${travel_hotel:.2f}') #Displays the estimated accomodation/hotel cost.
print(f'Food:               ${travel_food:.2f}') #Displays the estimated fuel cost.
print ('---------------------------------------') #Another line.

print(f'Remaining Balance:  ${travel_balance:.2f}') #Displays the remaining budget left over after all estimated costs have been subracted from the initial travel budget.
