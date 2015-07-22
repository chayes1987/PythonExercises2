__author__ = 'Conor'

"""
    Q 4.
    a) Write a Python application that takes a string as input from the user and passes the string to a function called
    reverse, which display the string in reverse order.
    (10 Marks)

    b) Write a Python application that takes employee details from a user and appends them to a file called
    employees.txt.

    The application should ask the user for the number of employee records they wish to create and then ask for the ID
    number and employee name for each record. The application should also be able to read data from employees.txt and
    display its contents on screen.
    (15 Marks)
"""

# A.4 (a)


# Reverse function
def reverse(string):
    return string[::-1]

# Take input and call function
user_input = input('Enter a string: ')
print(reverse(user_input))

# A.4 (b)

number_employees = input('How many employees do you wish to create? ')

for num in range(0, int(number_employees)):
    employee_id = input('Enter employee id: ')
    employee_name = input('Enter employee name: ')

    # Try block to catch exceptions
    try:
        # Open file, a for append mode
        my_file = open('c:\employees.txt', 'a')
        # Append
        my_file.write(employee_id + ' - ' + employee_name + '\n')
        # Close
        my_file.close()
    except Exception:
        pass

# Open in read mode to show contents
print(open('c:\employees.txt', 'r').read())