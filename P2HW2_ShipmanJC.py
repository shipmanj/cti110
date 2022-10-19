# A grade calculator.
# 10-19-2022
# CTI-110 P2HW2-Travel
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

#Enter students grade for module one. 
#Enter students grade for module two. 
#Enter students grade for module three. 
#Enter students grade for module four. 
#Enter students grade for module five. 
#Enter students grade for module six. 



#Make a list of the students grades starting from module 1 through module six.
#Combine the students grades from module one through module six to make the total sum.
#Divice the total sum of the students grades by the amount of grades, in this case six.


#Display the students lowest scored grade.
#Display the students highest scored grade.
#Display the studentss combined score of all of the students six grades.
#Display the students average score after diving the total sum by six.





#------------------------------------------------------------------
# Grade Inputs.
print ('___________________________________________________________________')
print ('This program calculates and displays travel expenses.') 
m1 = float(input('Enter Grade for Module 1: ')) 
m2 = float(input('Enter Grade for Module 2: ')) 
m3 = float(input('Enter Grade for Module 3: ')) 
m4 = float(input('Enter Grade for Module 4: ')) 
m5 = float(input('Enter Grade for Module 5: '))
m6 = float(input('Enter Grade for Module 6: ')) 


# Background Calculations
gradelist = [m1, m2, m3, m4, m5, m6]
gradesum = m1 + m2 + m3 + m4 + m5 + m6
gradeavg = gradesum / 6


# Results
print ('------------Results------------')
print(f'Lowest Grade:       {min(gradelist):}')
print(f'Highest Grade:      {max(gradelist):}')
print(f'Sum of Grades:      {gradesum:}') 
print(f'Average:            {gradeavg:.2f}')
print('--------------------------------------------------')
