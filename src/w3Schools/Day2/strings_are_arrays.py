'''
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''


def string_array():
    global name
    name = "Team Bharat"
    print("Length of name is : ", len(name))

    for i in name:
        print(i)

string_array()