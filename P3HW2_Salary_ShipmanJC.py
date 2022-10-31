# A salary calculator.
# 10-31-2022
# CTI-110 P3HW2-Salary
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

#Enter the employee's name. 
#Enter the hours worked.
#Enter the pay rate.

#If the hours worked exceeds 40 then calculate for overtime.
#If the hours worked is under 40 then overtime is not calculated
#Calculate the employee's regular pay based on hours worked.
#Calculate the employee's gross pay.
#Display employee's hours worked, pay rate, overtime, and all of their pay. 

#--------------------------------------------------------------------------------------------------------------------
# This program calculates an employee's salary and any overtime they have accrued.

# Enter employee information that is requested.

employee_name =  (input("Enter employee's name: "))
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("--------------------------------------------------")

#Calculate the employee's enter information to regular pay and any possible overtime.


if hours_worked > 40:
     ot_hours = hours_worked - 40
     reg_hours = 40
     ot_pay = (ot_hours * 1.5) * pay_rate
else:
     ot_hours = 0
     reg_hours = hours_worked
     ot_pay = 0



reg_pay = reg_hours * pay_rate
gross_pay = ot_pay + reg_pay

# Display results of all calculations.


print (f'Employee name:    {employee_name}')
print ("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f'{hours_worked:<16.1f}{pay_rate:<12.2f}{ot_hours:<12.1f}${ot_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:.2f}')

