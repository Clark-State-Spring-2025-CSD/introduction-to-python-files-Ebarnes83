#Eric Barnes Pythin 01/29/2025
#Print a line asking the user to enter three numbers
#Prompt the user to enter the three integers, one at a time
#Display the three numbers entered, their sum, and the average.
#You can assume the user will only enter positive integers
#Example output: (you do not have to match my words exactly)
#Please enter three whole numbers:
#Number 1: 11
#Number 2: 11
#Number 3: 12
#The sum of 11 and 11 and 12 is 34 and the average is 11.333333333333334.

number1 = 0
number2 = 0
number3 = 0

print("Please enter 3 numbers")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))

sum = number1 + number2 + number3
average = sum / 3

print(f"The sum of {number1} and {number2} and {number3} is {sum}")
print(f"The average of {sum} is {average}")
