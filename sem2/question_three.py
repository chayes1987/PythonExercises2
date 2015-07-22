__author__ = 'Conor'

"""
Q 3.
    a) Write a Python program that lets a user enter a series of 10 numbers. The program should store the numbers in a
    list and display the following data:

    • The highest number in the list.
    • The lowest number in the list.
    • The sum of the numbers in the list.
    • The average of the numbers in the list.
    (15 Marks)

    b) Write an application using Python, which generates six random numbers for a lottery. Each of the six random
    numbers generated should be in the range of 1 to 20 and should be stored in a list. The application should convert
    the list to a tuple and display the tuple containing the six lottery numbers on the screen.
    (10 Marks)
"""

# A.3 (a)

# Initialize empty list
numbers = []

# Read in the 10 numbers
for num in range(0, 10):
    number = input('Enter a number: ')
    numbers.append(int(number))

# Display required data, max, min, sum, and average
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sum(numbers) / len(numbers))


# A.3 (b)

# Import required package
from random import randint

lotto_nums = []

# Loop runs 6 times
for num in range(1, 7):
    # Generate random number
    random_num = randint(1, 20)
    # Add to list
    lotto_nums.append(random_num)

# Convert to tuple and display
print(tuple(lotto_nums))





