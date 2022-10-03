# Driving Cost Calculator
# 10-03-2022
# CTI-110 P2LAB-Driving Cost
# JC Shipman
#

gas_mileage = float(input())
gas_cost = float(input())
gas_distance1 = 20
gas_distance2 = 75
gas_distance3 = 500


gas_sum1 = (gas_cost / gas_mileage) * gas_distance1
gas_sum2 = (gas_cost / gas_mileage) * gas_distance2
gas_sum3 = (gas_cost / gas_mileage) * gas_distance3

print(f'{gas_sum1:.2f} {gas_sum2:.2f} {gas_sum3:.2f}')
