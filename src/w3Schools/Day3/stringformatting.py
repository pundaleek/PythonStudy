'''
To make sure a string will display as expected, we can format the result with the format() method.
String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
'''

user_input = int(input("Enter a number : "))

if (user_input%2) == 0:
    print(("Given number {} is Even").format(user_input))

else:
    print(("Given number {} is Odd").format(user_input))