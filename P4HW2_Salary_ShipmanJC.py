# A salary calculator.
# 11-18-2022
# CTI-110 P4HW2-Salary Calculator
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

#Enter the employee's name or enter None if you wish for program to stop.

#If a name was enter then program continues below.
#Enter the hours worked.
#Enter the pay rate.

#If the hours worked exceeds 40 then calculate for overtime.
#If the hours worked is under 40 then overtime is not calculated
#Calculate the employee's regular pay based on hours worked.
#Calculate the employee's gross pay.
#Display employee's hours worked, pay rate, overtime, and all of their pay.

#If you entered None then the program will end.

#--------------------------------------------------------------------------------------------------------------------
# This program calculates an employee's salary and any overtime they have accrued.

# Enter employee information that is requested.

ot_total = []
reg_total = []
gross_total = []
employee_count = 0

employee_name =  (input("Enter employee's name or enter None to terminate: "))

while employee_name != "None":    
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    employee_count = employee_count + 1
    if hours_worked > 40:
        ot_hours = hours_worked - 40
        reg_hours = 40
        ot_pay = (ot_hours * 1.5) * pay_rate
        reg_pay = reg_hours * pay_rate
        gross_pay = ot_pay + reg_pay
        reg_total.append(reg_pay)
        ot_total.append(ot_pay)
        gross_total.append(gross_pay)
        print (f'Employee name:    {employee_name}')
        print ("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
        print("-------------------------------------------------------------------------------------")
        print(f'{hours_worked:<16.1f}{pay_rate:<12.2f}{ot_hours:<12.1f}${ot_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:.2f}')
    else:
        ot_hours = 0
        reg_hours = hours_worked
        ot_pay = 0
        reg_pay = reg_hours * pay_rate
        gross_pay = ot_pay + reg_pay
        reg_total.append(reg_pay)
        gross_total.append(gross_pay)
        print (f'Employee name:    {employee_name}')
        print ("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
        print("-------------------------------------------------------------------------------------")
        print(f'{hours_worked:<16.1f}{pay_rate:<12.2f}{ot_hours:<12.1f}${ot_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:.2f}')
    employee_name =  (input("Enter employee's name or enter None to terminate: "))


            
print (f'Total number of employees entered:${employee_count}')
print (f'Total amount payed for overtime: ${sum(ot_total)}')
print (f'Total amount payed for regular hours: ${sum(reg_total)}')
print (f'Total amount payed in gross: ${sum(gross_total)}')
