"""
**** Python Lists ****
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:[] or list() 

**** List Items ****
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""
# mylist = ["apple", "banana", "cherry"]
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(mylist)

"""
**** List Length ****
To determine how many items a list has, use the len() function:
"""
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

"""
**** Access List Items *****
List items are indexed and you can access them by referring to the index number:
**** Negative Indexing ****
Negative indexing means start from the end

**** Range of Indexes or Slicing ****
You can specify a range of indexes by specifying where to start and where to end the range.
"""
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[1])  # returns apple
# print(thislist[-1])  # return cherry
# print(thislist[2:5]) #return cherry,orange,kiwi
# print(thislist[2:]) #This example returns the items from "cherry" to the end:
# print(thislist[:5]) #This example returns the items from the beginning to, but NOT including, "kiwi":
# print(thislist[-4:-1]) #This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

"""
**** Check if Item Exists ****
To determine if a specified item is present in a list use the in keyword:
"""
# thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

"""
**** Change Item Value ****
To change the value of a specific item, refer to the index number:
"""
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[1])
# thislist[1] = "blackcurrant"
# print(thislist)

"""
***** Change a Range of Item Values ****
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
"""
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

"""
**** Insert Items ****
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
"""
# thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
# thislist.insert(2, "watermelon")
# print(thislist)

"""
**** Append Items ****
To add an item to the end of the list, use the append() method:
"""
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

"""
**** Extend List ****
To append elements from another list to the current list, use the extend() method.
"""
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)  # Add the elements of tropical to thislist:
# print(thislist)

"""
**** Add Any Iterable ****
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

"""
**** Remove Specified Item ****
The remove() method removes the specified item.
"""
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

"""
**** Remove Specified Index ****
The pop() method removes the specified index.
If you do not specify the index, the pop() method removes the last item.
"""
# thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
# thislist.pop(1)
# thislist.pop() #remove last index
# del thislist[4] #The del keyword also removes the specified index:
# del thislist #The del keyword can also delete the list completely.
# print(thislist)

"""
**** Clear the List ****
The clear() method empties the list.
The list still remains, but it has no content.
"""
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

"""
**** Loop Through a List ****
You can loop through the list items by using a for loop:
"""
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

"""
Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

"""
****  Using a While Loop ****
You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
"""
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

"""
**** Looping Using List Comprehension ****
List Comprehension offers the shortest syntax for looping through lists:
"""
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

"""
**** List Comprehension ****
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
The Syntax
newlist = [expression for item in iterable if condition == True]
"""
# Without list comprehension you will have to write a for statement with a conditional test inside:

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# With list comprehension you can do all that with only one line of code:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# newlist = [x for x in fruits if x != "apple"] #Only accept items that are not "apple":
# newlist = [x for x in fruits] #With no if statement:
# newlist = [x for x in range(10)] #You can use the range() function to create an iterable:
# newlist = [x for x in range(10) if x < 5] #Accept only numbers lower than 5:
# newlist = [x.upper() for x in fruits] #Set the values in the new list to upper case:

# print(newlist)

"""
**** Sort List Alphanumerically ****
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort() #Sort the list alphabetically:
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort() #Sort the list numerically:
# print(thislist)

"""
***** Sort Descending ****
To sort descending, use the keyword argument reverse = True:
"""
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)#Sort the list descending:
# print(thislist)

"""
**** Reverse Order ****
What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.
"""
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

"""
**** Copy a List ****
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
"""
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# mylist = list(thislist) #Another way to make a copy is to use the built-in method list().
# print(mylist)

"""
***** List Methods ****
Python has a set of built-in methods that you can use on lists.
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
