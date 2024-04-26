# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
# def function(l):
#     try:
#         sum=0
#         for x in l:
#             sum+=x
#         return sum
#     except AttributeError:
#         print("Attribute error occured")
# print(function([1,2,3,4,5]))


class MyClass:
    try:
        def __init__(self):
            self.attribute_name = 5
    except AttributeError:
        print("AttributeError occured")
obj = MyClass()
print(obj.attribute_name)
# print(obj.c)

# Implement a function that calculates the square root of a given number. Handle any ValueError that may occur if the input number is negative
def squareroot(n):
    try:
        if n <0:
            raise ValueError("number is negative enter the number greater than zero")
        st=(n**(1/2))
        print(f"Square root of {n} is {st}")
    except ValueError as e:
        print(e)

print(squareroot(81))
print(squareroot(-9))

"""Create a dictionary with some key-value pairs. 
Write a program that prompts the user to enter a key and then prints the corresponding value. 
Handle the KeyError exception if the key does not exist in the dictionary."""
d={"Name":"Siya","Age":23,"ID":2}
def dictionary(k):
    try:
        print(d[k])
    except KeyError:
        print("You enter the wrong key\n")
print(dictionary("Siya"))
print(dictionary("ID"))

# Write a function that takes user input for their age and validates if it is a valid integer. Handle the ValueError exception if the input is not a number.

def age():
    try:
        n = int(input("Enter the age : "))
        print(f"Age of a person : {n}")
    except ValueError:
        print("Invalid Input. Enter the correct age")
print(age())
print(age())

# Write a program that prompts the user to enter their name and then prints a greeting. Handle the KeyboardInterrupt exception if the user cancels the input.

def msg():
    name=input("Enter the name : ")
    try:
        print(f"Welcome, {name}")
    except KeyboardInterrupt:
        print("Cancel the program")

print(msg())
print(msg())


