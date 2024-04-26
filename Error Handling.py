print("Welcome")
# # IndentationError
#     print("Hello")
# # Logical Error : NameError: name 'c' is not defined
# a = 10
# b = 20
# print("Addition:", a + c)

# The FilenotfoundError is raised when a file in not present on the disk
# f=open("text.txt")
# print(f)

# ZeroDivisionError: division by zero
# a = 10
# b = 0
# c = a / b
# print("a/b = %s" % c)

#  try-except block
try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=a/b
    print("Answer : ",c)
except:
    print("can not divide by zero")

# syntax error (colon is not provided after if condition)
# a=10
# if a>5
#     print(a,"is greater than 5")
#

# type error (can not work + operand for string and integer)
# a=30
# b="Siya"
# print(a+b)

try:
    a=30
    b="Riya"
    c=a+b
    print("Answer : ",c)
except:
    print("can not add string and integer")


try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a / b
    print("Answer : ", c)
except ValueError:
    print("Enter the correct value")
except ZeroDivisionError:
    print("can not divide by zero")


# Handle multiple exceptions with a single except clause
try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a / b
    print("Answer : ", c)
except (ValueError, ZeroDivisionError):
    print("Enter the correct value")


try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a / b
    print("Answer : ", c)
except ValueError:
    print("Enter the correct value")
except ZeroDivisionError:
    print("can not divide by zero")
finally:
    print("Done!!!!")


try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("a/b = %s" % c)

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("We are in else block ")