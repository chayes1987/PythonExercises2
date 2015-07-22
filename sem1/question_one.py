__author__ = 'Conor'

"""
    Q.1 Write a Python program that reads in 12 monthly sales figures from a user and displays the annual total as well
     as an average monthly sales figure.

    A sample of the program running:

    Enter the sales for month 1: 45
    Enter the sales for month 2: 78
    …
    Enter the sales for month 12: 67

    Annual sales = 650
    Average monthly sales = 54.17

    (25 marks)
"""

# A.1

# Initialize total variable
total = 0

# Create loop for the 12 inputs
for num in range(1, 13):
    # Read in and add to the total
    sales_figure = input('Enter the sales for month %s: ' % num)
    # Type cast to integer and add to total
    total += int(sales_figure)

# Print the total and average
print('\nAnnual Sales = %s\nAverage monthly sales = %s' % (total, round(total / 12, 2)))