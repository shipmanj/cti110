# A grade calculator.
# 10-26-2022
# CTI-110 P3HW1-Debugging
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

#Enter students grade for modules one trhough six. 



#Make a list of the students grades starting from module 1 through module six.
#Combine the students grades from module one through module six to make the total sum.
#Divice the total sum of the students grades by the amount of grades, in this case six.


#Display the students lowest scored grade, their highest scored grade, the combined sum of their grads, and the average score after dividing by six(amount of grades entered.)
#Display the students letter grade.
#--------------------------------------------------------------------------------------------------------------------
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = (sum / len(grades))

# Results

print ('------------Results------------')
print(f'Lowest Grade:       {min(grades):}')
print(f'Highest Grade:      {max(grades):}')
print(f'Sum of Grades:      {sum:}') 
print(f'Average:            {avg:.2f}')
print('--------------------------------------------------')

# Determine letter grade for average

if avg >= 90:
    print ("Your grade is: A")
elif avg >= 80:
    print('Your grade is: B')
else:
    print('Your grade is: F')






