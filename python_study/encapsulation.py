"""
================  Encapsulation ================
Encapsulation means wrapping of data and methods into a single unit.
## Access Modifier 

=> Public (No Modifier): Class members (attributes and methods) without any access modifier are considered public and can be accessed from outside the class.

=> Protected (_): Members prefixed with an underscore (e.g., _variable) are considered protected and should not be accessed directly from outside the class. However, it's more of a naming convention to indicate that the member is intended for internal use.

=>Private (__): Members prefixed with double underscores (e.g., __variable) are considered private and should not be accessed directly from outside the class. Python enforces name mangling to make it more difficult to access private members.

"""
class Person:
    #constructor method
    def __init__(self, name, age):
        self.__name=name ## Private attribute
        self.__age =age # Private attribute

    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age} ")




#rameshObj = Person('Ramesh',34)
#print(dir(rameshObj)) # get all attribute and function list
#print(rameshObj._Person__name) # access private variable
#rameshObj.display_info() # call a object function


""" 
Constructor Method Define 

"""
class Mobile:
    def __init__(self, model, price):
        self.model =model
        self.price =price
        print("Mobile Constructor Called automatically when create a instance")

    
    def show_model(self):
        print(f"Model Name is {self.model} and Price is {self.price}")


realme =Mobile('Realme', 10000)
realme.show_model()