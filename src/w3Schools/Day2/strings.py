"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

# p1 - You can display a string literal with the print() function
# p2 - Assign String to a Variable
# p3 - Multiline Strings
# p4 - String are Arrays
"""

# p1
print("hello")
print('hello')

# p2
country_name = "Bharat"
print("My country name is ", country_name)

# p3
description = """My name is Pundalik,
I am from Vijayapura,
I am working as Software Engineer"""

task = '''
Write a python program,
to add 2 numbers, & divide them.
While doing subtraction and multiplication.
'''

print(description)
print(task)

'''
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''

about_python = "Python is a great programming language"
print(about_python)