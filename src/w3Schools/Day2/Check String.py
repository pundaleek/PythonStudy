'''
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
'''
user_str = "Py"
text = "I Love Python!!"

if user_str in text:
    print(user_str, " is present in a string")

else:
    print(user_str, " is not present in a string")

'''
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
'''
user_input = "Java"
dummyText = "I Love Python!!"

if user_input not in dummyText:
    print(user_input, " is ABSENT in a string")

else:
    print(user_input, " is present in a string")