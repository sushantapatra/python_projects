"""
**** Python Strings ****
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'Hello' or "Hello"

**** Strings are Arrays ****
Square brackets [] can be used to access elements of the string.
Get the character at position 1 (remember that the first character has the position 0):
"""
# name ="Sushanta patra"
# print(name[0])

"""
**** Looping Through a String ****
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""
# for x in "banana":
#   print(x)

"""
**** String Length ****
To get the length of a string, use the len() function.
"""
# a = "Hello, World!"
# print(len(a))

"""
**** Check String ****
To check if a certain phrase or character is present in a string, we can use the keyword in

"""
# txt = "The best things in life are free!"
# print("free" in txt)

# if "free" in txt:
#   print("Yes, 'free' is present.")

"""
**** Check if NOT ****
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
"""
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

"""
**** Slicing ****
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
# b = "Hello, World!"
# print(b[0:5]) #Hello
# print(b[:5]) #Hello
# print(b[2:5]) #llo
# print(b[2:]) #llo, World!
# print(b[-6:-1]) #world
# print(b[:-1]) #Hello, World!

"""
===== Python - Modify Strings =======
**** Upper Case ****
The upper() method returns the string in upper case:
"""
# a = "Hello, World!"
# print(a.upper())

"""
**** Lower Case ****
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
"""
# a = "Hello, World!"
# print(a.lower()) 

"""
**** Replace String ****
The replace() method replaces a string with another string:
"""
# a = "Hello, World!"
# print(a.replace("H", "J")) # returns Hello, World!

"""
**** Split String ****
The split() method returns a list where the text between the specified separator becomes the list items.
"""
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

"""
**** String capitalize() Method ****
The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
"""
# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

"""
**** String casefold()() Method ****
The casefold() method returns a string where all the characters are lower case.
"""
# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print (x)

"""
**** String center() Method ****
The center() method will center align the string, using a specified character (space is default) as the fill character.
"""
# txt = "Hello this is string"
# x = txt.center(100)
# print (x)

"""
**** String encode() Method ****
The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
"""
# txt = "My name is Ståle"
# x = txt.encode()
# print (x)

"""
**** String endswith() Method ****
The endswith() method returns True if the string ends with the specified value, otherwise False.
Syntax => string.endswith(value, start, end)
value   =>	    Required. The value to check if the string ends with
start   =>	    Optional. An Integer specifying at which position to start the search
end	    =>      Optional. An Integer specifying at which position to end the search
"""
# txt = "My name is sushanta"
# x = txt.endswith('sushanta') # return true
# y = txt.endswith('sushanta',5,10) #return false
# print (x,y)
"""
**** String find() Method ****
The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

Syntax  => string.find(value, start, end)
value   =>	Required. The value to search for
start   =>	Optional. Where to start the search. Default is 0
end     =>	Optional. Where to end the search. Default is to the end of the string
"""
# txt = "Hello, welcome to my world."
# x = txt.find("e")
# print(x)

"""
**** String format() Method ****
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
The format() method returns the formatted string.

Syntax  =>  string.format(value1, value2...)
value1, value2...	=> Required. One or more values that should be formatted and inserted in the string.
                    => The values are either a list of values separated by commas, a key=value list, or a combination of both.
                    => The values can be of any data type.
"""
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1,txt2,txt3, sep="\n")

"""
**** String index() Method ****
The index() method finds the first occurrence of the specified value.
The index() method raises an exception if the value is not found.
The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. 
Syntax => string.index(value, start, end)
"""
# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# y = txt.index("e", 5, 10)
# print(x,y)

"""
txt = "Company12"
myTuple = ("John", "Peter", "Vicky")

isalnum()	Returns True if all characters in the string are alphanumeric   =>txt.isalnum()
isalpha()	Returns True if all characters in the string are in the alphabet    =>txt.isalpha()
isascii()	Returns True if all characters in the string are ascii characters   =>txt.isascii()
isdecimal()	Returns True if all characters in the string are decimals       => txt.isdecimal()
isdigit()	Returns True if all characters in the string are digits         =>txt.isdigit()
isidentifier()	Returns True if the string is an identifier     =>txt.isidentifier()
islower()	Returns True if all characters in the string are lower case =>txt.islower()
isnumeric()	Returns True if all characters in the string are numeric    =>txt.isnumeric()
isprintable()	Returns True if all characters in the string are printable  =>txt.isprintable()
isspace()	Returns True if all characters in the string are whitespaces    =>txt.isspace()
istitle()	Returns True if the string follows the rules of a title =>txt.istitle()
isupper()	Returns True if all characters in the string are upper case     =>txt.isupper()
join()	Converts the elements of an iterable into a string      =>x = "#".join(myTuple) //string.join(iterable)
ljust()	Returns a left justified version of the string  =>txt.ljust(20)
lower()	Converts a string into lower case   =>txt.lower()
lstrip()	Returns a left trim version of the string   =>txt.lstrip()
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value =>txt.replace("bananas", "apples")
rfind()	Searches the string for a specified value and returns the last position of where it was found   =>txt.rfind("casa")
rindex()	Searches the string for a specified value and returns the last position of where it was found   =>txt.rindex("casa")
rjust()	Returns a right justified version of the string     =>txt.rjust(20)
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list    =>txt.rsplit(", ")
rstrip()	Returns a right trim version of the string  =>txt.rstrip()
split()	Splits the string at the specified separator, and returns a list =>txt.split()
splitlines()	Splits the string at line breaks and returns a list =>txt.splitlines()
startswith()	Returns true if the string starts with the specified value  =>txt.startswith("Hello")
strip()	Returns a trimmed version of the string     =>txt.strip()
swapcase()	Swaps cases, lower case becomes upper case and vice versa   =>txt.swapcase()
title()	Converts the first character of each word to upper case =>txt.title()
translate()	Returns a translated string
upper()	Converts a string into upper case   =>txt.upper()
zfill()	Fills the string with a specified number of 0 values at the beginning
"""


"""
**** Escape Characters ****
\'	=>  Single Quote	
\\	=>  Backslash	
\n	=>  New Line	
\r	=>  Carriage Return	
\t	=>  Tab	
\b	=>  Backspace	
\f	=>  Form Feed	
\ooo =>	Octal value	
\xhh    =>	Hex value
"""





"""
**** Formatting Types ****

:<	=>	Left aligns the result (within the available space)
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49)) #return We have 49     chickens.

:>	=>	Right aligns the result (within the available space)
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))


:^	=>	Center aligns the result (within the available space)
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))

:=	=>	Places the sign to the left most position
#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5)) #returns We have    49    chickens.

:+	=>	Use a plus sign to indicate if the result is positive or negative
#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7)) returns The temperature is between -3 and +7 degrees celsius.

:-	=>	Use a minus sign for negative values only
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7)) #returns The temperature is between -3 and 7 degrees celsius.

: 	=>	Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7)) #returns The temperature is between -3 and  7 degrees celsius.

:,	=>	Use a comma as a thousand separator
#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000)) #returns The universe is 13,800,000,000 years old.

:_	=>	Use a underscore as a thousand separator
#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000)) #returns The universe is 13_800_000_000 years old.

:b	=>	Binary format
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5)) #returns The binary version of 5 is 101

:c	=>	Converts the value into the corresponding unicode character

:d	=>	Decimal format
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101)) #returns We have 5 chickens.

:e	=>	Scientific format, with a lower case e
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5)) #returns We have 5.000000e+00 chickens.

:E	=>	Scientific format, with an upper case E
#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5)) #returns We have 5.000000E+00.

:f	=>	Fix point number format
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45)) #returns The price is 45.00 dollars.

#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45)) #returns The price is 45.000000 dollars.

:F	=>	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))

:g	=>	General format
:G	=>	General format (using a upper case E for scientific notations)
:n	=>	Number format
:%	=>	Percentage format
#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25)) #returns You scored 25.000000%

#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25)) # returns You scored 25%
"""