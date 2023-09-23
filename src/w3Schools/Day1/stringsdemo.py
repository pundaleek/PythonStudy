"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""

# print("Hello")
# print("'Hello'")

# print(type("hello"))
# print(type("'hello'"))

name = "Appu"
# print(name)

# Multiline string representation
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(a)

x = "Namaste, Vijayapura!!"
print(len(x))

# print(x[10])

# for i in "Namaste, Vijayapura!!":
#     # print(i)

txt = "The best things in life are free!"
print("free" in txt)