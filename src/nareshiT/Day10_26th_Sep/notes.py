'''
26th September 2023

Data types & Literals

A litral is constant or value which never changes.
Python literals are classified into 2 categories:
    1. Numeric Literals 
        a. Integer literals
        b. Float literals
        c. Complex literals

    2. Non Numeric Literals
        a. String
        b. Boolean
        c. None

What is a Data Type?

Data types are used to allocate or reserve memeory for literals or values.
Python data types 
    1. Scalar Data Types are used to resrve memory for one value
        i. Int
        ii. Float
        iii. Complex
        iv. Bool
        v. NoneType                                                                                                                                                
    2. Collection Data Types (or Data Structures) represents more than one value. 
    Python collection types are classified into different categories:
        1. Sequences:
            i. List
            ii. Tuple
            iii. Range
            iv. String
            v. Bytes
            vi. bytesarray

        2. Sets:
            i. Set
            ii. frozenset

        3. Mapping:
            i. Dictionary 

    Scalar data types & collection data types are called std data types of python.
    These data types come with python language

    What is variable?
    Vraibale is an Identifire, this is used to identify the value. 
    Variables are named memeory loaction. The value of variable can be changed. 
    Vraibles are bind with data type.

    Python is dynamically typed prgramming language, there are no var declarations. 
    Var are not bind with one type, type is cahnges based on the value or object.

    int data type

    int is a scalara data type
    Size of int is unlimited; python virtual machine allocates memory based on vlaue size
    How to find size & type of var?
    Finding size?
        import sys
        sys.getsizeof(var name)

    Finding type?
        type(var name)
'''