__author__ = 'Conor'

"""
    Q.2 Write a Python program that reads in a day of the week from the user and prints out the name of the next day.

    A sample of the program running:

    Enter a day of the week: Tuesday Tomorrow is Wednesday

    Your code should work for all 7 days.

    (25 marks)
"""

# A.2

# Initialize a list of the months of the year
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# Get the input from the user
day = input('Enter a day: ')

# Check for Sunday and set index to Monday
if 'sunday' == day.lower():
    index = 0
else:
    # Otherwise set index to current month + 1 position
    index = days.index(day.lower()) + 1

# Print the output (title() function will capitalize the first letter)
print('%s Tomorrow is %s' % (day, days[index].title()))