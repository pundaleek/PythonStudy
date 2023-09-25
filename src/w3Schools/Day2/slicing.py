'''
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
Note: The first character has index 0.
'''

text = "Namma Kannada. Kasturi Kannada"

print("Pre Slice :", text)

sliced_word = text[0:14]

print("Post slice : ", sliced_word)
print("Kannada" in sliced_word)
print("Telugu" not in sliced_word)

# Slice from the start
sliced_from_start = text[:10]
print(sliced_from_start)

# Slice To the End
sliced_till_end = text[15:]
print(sliced_till_end)

# Negative Indexing
negative_indexing = text[-6:-2]
print(negative_indexing)