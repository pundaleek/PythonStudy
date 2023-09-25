'''
String Concatenation
To concatenate, or combine, two strings you can use the + operator.
'''
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

'''
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
'''

age = 18
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 82.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))

'''
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
'''
txt1 = "We are the so-called \"Vikings\" from the north."
print(txt1)