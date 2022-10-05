# Driving Cost Calculator
# 10-05-2022
# CTI-110 P2LAB-Stats
# JC Shipman
#

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num_multiply = num1 * num2 * num3 * num4
num_average = (num1 + num2 + num3 + num4) / 4

print(f'{num_multiply:.0f} {num_average:.0f}')
print(f'{num_multiply:.3f} {num_average:.3f}')
