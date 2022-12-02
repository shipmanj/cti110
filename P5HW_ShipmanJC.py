# A math quiz program.
# 12-1-2022
# CTI-110 P5HW2-Math Quiz
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

#This program presents math quizzes.

#Ask user to slecet a quiz from the menu or exit the program.
#When a quiz is selected the user is presented with a math problem.
#If the user enters the wrong answer they will be asked to try again until they get the right answer.
#Once the user has entered the right answer they will be returned to the main program selection menu.
#---------------------------------





import random
print('Welcome to Math Quiz\n\n')

def math_menu():
    print("MAIN MENU")
    print("--------------------------")
    print('1. ) Adding Random Numbers')
    print('2. ) Subtracting Random Numbers')
    print('3. ) Exit\n')

quit_program = False

while not quit_program :
    math_menu()
    choice = int(input('Please choose one of the menu options: '))
    if choice == 3 :
        print('Thank you for playing...\nBye!!')
        quit_program = True
    else :
        if choice == 1 :
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            addition = number1 + number2
            print(f'  {number1}\n+ {number2}')
            answer = int(input('Enter answer.\n'))
            guess = 1
            while answer != addition :
                if answer < addition :
                    guess += 1
                    print('Sorry, guess is too low.')
                elif answer > addition :
                    guess += 1
                    print('Sorry, guess is too high.')
                answer = int(input('Try Again: '))
            print('Congratulations!!!! Your answer is correct..')
            print(f'Number of guesses: {guess}')
        elif choice == 2 :
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            subtraction = number1 - number2
            print(f'  {number1}\n- {number2}')
            answer = int(input('Enter answer.\n'))
            guess = 1
            while answer != subtraction :
                if answer < subtraction :
                    guess += 1
                    print('Sorry, guess is too low.')
                elif answer > subtraction :
                    guess += 1
                    print('Sorry, guess is too high.')
                answer = int(input('Try Again: '))
            print('Congratulations!!!! Your answer is correct..')
            print(f'Number of guesses: {guess}')
        print()
