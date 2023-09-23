"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
name = "Pundalik"
city = "Vijayapura"
country = "Bharat"
state = "Karnataka"


def print_my_name():
    print("My name is : " + name)


def print_my_country():
    print("My state " + state + " is in " + country)


def print_my_city():
    print("I am from " + city)


def print_my_state():
    print("My city " + city + " is in " + state + " state")


# print_my_name()
# print_my_city()
# print_my_state()
# print_my_country()

"""
The global Keyword
Normally, when we create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, we can use the global keyword.
"""
myFavMovie = "Jailer"
def demo_global_keyword():
    global myFavMovie
    myFavMovie = "Sholay"
    myFavHero = "Super Star Rajini"
    print("My fav movie is : " + myFavMovie)
    print("My fav her is : " + myFavHero)

demo_global_keyword()

myFavTheatre = "Urvashi"
print("I watched my fav movie " + myFavMovie + " in my fav theatre " + myFavTheatre)