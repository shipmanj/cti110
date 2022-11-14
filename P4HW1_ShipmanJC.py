# A grade calculator.
# 11-17-2022
# CTI-110 P4HW1-Score List
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

#Ask user for amount of scores they wish to enter.
#Ask user for scores until they enter all the scores they told the program they would enter.
#If a score is invalid, keep prompting the user to enter a valid score.
#Once all scores are entered, display the lowest score entered.
#Display all the scores with the lowest score removed.
#Display the average of all the scores.
#Display a letter grade based on the average score.





#------------------------------------------------------------------
# Score Inputs.

ScoreAmount = int(input("How many scores do you want to enter?:"))
ScoreNumber = 0
ScoreList = []
InvalidList = []
Score = 0
        


for i in range (ScoreAmount):
    ScoreNumber = ScoreNumber + 1
    Score = float(input(f'Enter score #{ScoreNumber}: '))
    if 100 >= Score >= 0:        
        ScoreList.append(Score)
        continue
    elif Score < 0:                
        while Score < 0:
            print ("INVALID Score entered!!!!")
            print ("Score should be between 0 and 100")
            Score = float(input(f'Enter Score #{ScoreNumber} again: '))
            if 100 >= Score >= 0:
                ScoreList.append(Score)
            else:
                continue
        continue
    else:
        print()
            

print ('----------------Results----------------')
print(f'Lowest Score    : {min(ScoreList):}')
ScoreList.remove(min(ScoreList))
ScoreAvg = sum(ScoreList) / len(ScoreList)
print(f'Modified List   : {ScoreList:}')
print(f'Scores Average  : {ScoreAvg:.2f}')
if ScoreAvg >= 90:
    print (f'Grade      : A')
elif ScoreAvg >= 80:
    print(f'Grade       : B')
elif ScoreAvg >= 70:
    print(f'Grade       : C')
elif ScoreAvg >= 60:
    print(f'Grade       : D')
else:
    print(f'Grade       : F')
print ('---------------------------------------')
