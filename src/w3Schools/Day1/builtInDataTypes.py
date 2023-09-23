"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

Getting the Data Type
You can get the data type of any object by using the type() function:
"""
# Setting the Data Type

x = "Appu!!"
print(type(x))

x = 200
print(type(x))

x = 200.5
print(type(x))

x = 1j
print(type(x))

x = ["PH", "KB", "VJ"]
print(type(x))

x = ("PH", "KB", "VJ")
print(type(x))

x = range(6)
print(type(x))

x = {"name": "Appu", "age": 39}
print(type(x))

x = {"PH", "KB", "VJ"}
print(type(x))

x = frozenset({"PH", "KB", "VJ"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))

# Setting the Specific Data Type
x = str("Hello Appu!!")
print(type(x))

x = int(20)
print(type(x))

x = float(100)
print(type(x))

x = str(400)
print(type(x))

