# Print all keyywords and count
import math
import keyword

list_keywords = keyword.kwlist

print(list_keywords)
print("Number of keywords : "+str(len(list_keywords)))

"""
# Identifiers in Python should NOT be:
1. Keyword
2. Variable
3. Module name
4. Funtion name
5. Package name
6. Start with digit (numeric)
7. There should not be any space
8. Only a special character is allowed is underscore (_)
9. Maximum length of an identifier is UNLIMITED
10. Case-sensitive

# Difference between Identifier and Keyword
"""

num = 5

factorial = math.factorial(num)

print("Factorial of " + str(num) + " is : " + str(factorial))
