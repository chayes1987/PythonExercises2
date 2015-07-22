__author__ = 'Conor'

"""
    Q 2.
    a) Write a Python program that counts and displays, the number of words in a sentence entered by the user. The
    program should identify a word as anything with space around it.
    (10 Marks)

    b) ACME Telecom require an application which will allow the company to gather together into one object, all of their
     customer names and telephone numbers as key-value pairs.

    You are required to write the program using Python and include the following:

    • an add function which can be used to add a key-value pair.
    • a search function which uses a key, given by the user to find a value.
    (15 Marks)
"""

# A.2 (a)
# Read the input

# Quick way
sentence = input('Enter your sentence: ')
if sentence == '':
    print('The number of words in the sentence is 0')
else:
    words = sentence.split(' ')
    print('The number of words in the sentence is: %s' % len(words))


# alternative way
def word_counter(string):
    word_count = 0
    # Empty
    if string == '':
        return word_count
    else:
        # Loop through string
        for char in string:
            # If space then count word before it
            if char == ' ':
                word_count += 1
        # Add one to return, sentence will always have one more word than space
        return word_count + 1

print('The number of words in the sentence is: %s' % word_counter(sentence))

# A.2 (b)

# Define dictionary (holds key, value pairs)
customer_details = {}
print(customer_details)


# Add customer function, number is the key
def add_customer(name, number):
    customer_details[number] = name


# Find customer function, return value for matching key
def find_customer(number):
    return customer_details[number]

# Add some customers
add_customer('Jane Doe', '0667185968')
add_customer('Joe Bloggs', '0667143558')

# Find some customers
print(find_customer('0667185968'))
print(find_customer('0667143558'))