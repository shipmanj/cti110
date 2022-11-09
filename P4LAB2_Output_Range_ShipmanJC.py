number1 = int(input())
number2 = int(input())

if number1 > number2:
    print ("Second integer can't be less than the first.")
    
elif number1 < number2:
    while number1 <= number2:
        print(number1, end=' ')
        number1 = number1 + 5
    print('')

else:
    print (number1, '')