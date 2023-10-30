# Write a program to print first 10 even numbers in reverse order

start_number = 2
max_number = 20

while max_number >= start_number:
    print(max_number, end=' ')
    max_number = max_number - 2

print()
# Write a program to print alphabets from A.....Z
# 1st find out ASCII values of alphabets

char = 'A'
ascii_A = ord(char)
# print(ascii_A)
# print(chr(ascii_A))

char = 'Z'
ascii_Z = ord(char)
# print(ascii_Z)
# print(chr(ascii_Z))

char = 'a'
ascii_a = ord(char)
# print(ascii_a)
# print(chr(ascii_a))

char = 'z'
ascii_z = ord(char)
# print(ascii_z)
# print(chr(ascii_z))

# while ascii_A <= ascii_Z:
#     print(chr(ascii_A), end=' ')
#     ascii_A = ascii_A + 1

# print()

# while ascii_a <= ascii_z:
#     print(chr(ascii_a), end=' ')
#     ascii_a = ascii_a + 1

# print()

while ascii_Z >= ascii_A:
    print(chr(ascii_Z), end=' ')
    ascii_Z = ascii_Z - 1

print()

# while ascii_a <= ascii_z:
#     print(chr(ascii_a), end=' ')
#     ascii_a = ascii_a + 1