__author__ = 'Conor'

"""
    Q 1.
    a) In relation to Python, outline the primary differences between a list and a tuple.
    (4 Marks)
    A. http://www.hacksparrow.com/python-difference-between-list-and-tuple.html
    b) With regard to Python, briefly describe the following types of exceptions and give examples as to where they are
    likely to occur.

    • ValueError
    • IndexError
    (6 Marks)
    A.  ValueError -> When receiving input, users entered character string instead of an integer
        IndexError -> Accessing an index in a list that doesn't exist e.g. nums = [1, 2, 3], print(nums[4])
    c) Write a program using Python, which allows the user to enter the name of a file and displays the contents of the
    file. The program should also handle exceptions associated with the opening of flies.
    (15 Marks)
"""

# A.1 (c)

# Create file c:\helloworld.txt with contents 'Hello World!'
name_of_file = input('Enter the name of your file: ')

# Try block to catch exceptions e.g. File doesn't exist
try:
    # Read file
    my_file = open(name_of_file)
    # Show contents
    print(my_file.read())
except FileNotFoundError:
    print('File \'%s\' does not exist.' % name_of_file)
    pass
