# A simple travel expense calculator/
# 09-26-2022
# CTI-110 P1HW2-Travel Expense
# JC Shipman
#

# Travel Inputs
print ('___________________________________________________________________')
print ('This program calculates and displays travel expenses.')
travel_budget = int(input('Enter Travel Budget:\n'))
travel_destination = input('Please enter travel destination:')
travel_gas = int(input('How much do you think you will spend on gas?:\n'))
travel_hotel = int(input('How much do you think accomodations will cost?:\n'))
travel_food = int(input('How much will you need for food?:\n'))

# Background Calculations
travel_cost = travel_gas + travel_hotel + travel_food
travel_balance = travel_budget - travel_cost


# Results
print ('------------Travel Expenses------------')
print ('Location:', travel_destination)
print ('Initial Budget:', travel_budget)

print ('Fuel:', travel_gas)
print ('Accomodation', travel_hotel)
print ('Food:', travel_food)

print ('Remaining Balance:', travel_balance)
print ('___________________________________________________________________')
