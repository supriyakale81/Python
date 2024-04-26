# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def division_error(a,b):
    try:
        c=a/b
        print("Answer : ",c)
    except ZeroDivisionError:
        print("can not divide by zero")
print(division_error(5,3))

print(division_error(5,0))


# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def value_error(a):
    try:
        if type(a)==int:
            return a
        else:
            raise ValueError("Value is not integer")
    except ValueError as e:
        print(e)
print(value_error(5))
print(value_error(4.7))
print(value_error('f'))

# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def file(filename):
    try:
        f=open(filename)
        c=f.read()
        f.close()
        return c
    except FileNotFoundError:
        print("file is not found ")
print(file(r"test.txt"))
print(file(r"C:\Users\Supriya\Downloads\death-rate-from-suicides-gho new.csv"))

# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def add(a,b):
    try:
        if type(a)==str or type(b)==str:
            raise TypeError("can not add string and integer ")
        c=a+b
        print("Addition is : ",c)
    except TypeError as e:
        print(e)

print(add(5,6))
print(add(6,'h'))


# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def pererror(filename):
    try:
        f=open(filename)
        c=f.read()
        f.close()
        return c
    except PermissionError:
        print("don't have permission to open file")

print(pererror(r"C:\Users\Supriya\Box"))
print(pererror(r"C:\Users\Supriya\Box\borr\Arabia i\10 DDR\MARJAN_854"))
# print(pererror(r"C:\Users\Supriya\Downloads\death-rate-from-suicides-gho new.csv"))

# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def List(l):
    try:
        i=int(input("Enter index : "))
        return l[i]
    except IndexError:
        print("Index is out of range. range of index is ",(0,len(l)-1))
print(List([3,4,6]))
print(List([23,5,6,7,5]))

# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input
import sys
def keyboard():
    try:
        num=int(input("Enter the number : "))
        print(num)
    except KeyboardInterrupt:
        print("user cancel the input")

print(keyboard())
print(keyboard())

#  Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def numbers(a,b):
    try:
        d=a/b
        print("answer : ",d)
    except ArithmeticError:
        print("Enter the correct value")

print(numbers(3,5))
print(numbers(5,0))
