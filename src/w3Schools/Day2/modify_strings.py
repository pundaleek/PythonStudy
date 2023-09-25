'''
Python - Modify Strings
Python has a set of built-in methods that you can use on strings.
Upper Case - upper()
Lower Case - lower()
Remove Whitespace - strip()
Replace String - replace()
Split String - split()
'''

text1 = "Namma Kannada!!"
print(text1.upper())

print(text1.lower())

text2 = " Namma Kannada!! "
print(text2.strip())

print(text1.replace("Namma", "Kasturi"))

original_text = "Namma Kannada, Namma Abhimana!!"
split_text = original_text.split(" ")
print(split_text)

for i in split_text:
    print(i)