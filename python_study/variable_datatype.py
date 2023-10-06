""" 
======= Python Data Types ===========

**** Built-in Data Types *****
Variables can store data of different types, and different types can do different things.

Text Type           :	str
Numeric Types       :	int, float, complex
Sequence Types      :	list, tuple, range
Mapping Type        :	dict
Set Types           :	set, frozenset
Boolean Type        :	bool
Binary Types        :	bytes, bytearray, memoryview
None Type           :	NoneType


Example 

x = "Hello World"                                   #str
x = 20                                              #int
x = 20.5                                            #float
x = 1j                                              #complex
x = ["apple", "banana", "cherry"]                   #list
x = ("apple", "banana", "cherry")                   #tuple
x = range(6)                                        #range
x = {"name" : "John", "age" : 36}                   #dict
x = {"apple", "banana", "cherry"}                   #set
x = frozenset({"apple", "banana", "cherry"})        #frozenset
x = True                                            #bool
x = b"Hello"                                        #bytes
x = bytearray(5)                                    #bytearray
x = memoryview(bytes(5))                            #memoryview
x = None                                            #NoneType
"""


"""
Variables
    Variables are containers for storing data values.
"""
# y = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(y) #4
# print(x) #salary
# print(x,y, sep=" - ",end=" This in end line ") #Sally - 4 This in end line
# print([x,y]) #['Sally', 4]

"""
Casting
If you want to specify the data type of a variable, this can be done with casting.
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

"""
******* Get the Type ******
You can get the data type of a variable with the type() function.
"""
# print(type(x))
# print(type(y))

"""
**** Case-Sensitive ****
Variable names are case-sensitive.
"""
# name ="Sushanta"
# Name= "Pagulu"
# print([name, Name]) #name will not overwrite Name

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John" 

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"

Python Variables - Assign Multiple Values
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
"""
# color, color2, color3 = "Orange", "Banana", "Cherry"
# print(color,color2,color3)


"""
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
"""
# color =color1=color2 ="Orange"
# print(color,color1,color2)
# print([color,color1,color2])

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""
# fruits = ["apple", "banana", "cherry","greps","orange","piannaple"]
# apple, banana,cherry, *others= fruits
# print(apple,banana,cherry,others) #apple banana cherry ['greps', 'orange', 'piannaple']

"""
**** Python - Global Variables ****
"""
# myName ="sushanta" #global variable
# def printName():
#     myName ="Pagulu" #local varible
#     print(myName)

# printName()
# print(myName)

"""
**** The global Keyword ****
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""
# def printName():
#     global myName
#     myName ="Pagulu"
   

# printName()
# print("my Global Name is : " + myName)
