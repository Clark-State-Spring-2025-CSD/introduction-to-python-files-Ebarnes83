#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the numbers
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

def analyze_numbers_file(filename):

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    numbers = []
    total = 0
    highest_number = float('-inf') 
    lowest_number = float('inf')   

    for line in lines:
        try:
            number = float(line.strip())

            numbers.append(number)

            total += number

            if number > highest_number:
                highest_number = number
            if number < lowest_number:
                lowest_number = number
        except ValueError:
            print(f"Warning: Skipping invalid number in line: {line.strip()}")

    if len(numbers) > 0:
        average = total / len(numbers)
    else:
        average = 0

    print(f"Number of numbers in the file: {len(numbers)}")
    print(f"Total of all numbers: {total}")
    print(f"Average of all numbers: {average}")
    print(f"Highest number: {highest_number}")
    print(f"Lowest number: {lowest_number}")

analyze_numbers_file('numbers.txt')
