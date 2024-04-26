def school(name):
    school_name="ABC School"  #local variable
    print(f"{name} completed education from {school_name}")

school("Seeta")
school("Geeta")
def student(name):
    print(f"{name} completed education from {school_name}")
# student("Seeta")
# student("Geeta")


# student function shows error because school name is local variable and we can not accessible it for student method.
b=8
def func():
    a=7
    print(a)
    print(b)
func()
# print(a)
# Write a Python program to detect the number of local variables declared in a function.

def fun():
    x=1
    y="Hello"
    z="Python"
    p=0.5
    q=input("Enter name : ")
    print(f"WELCOME {q.upper()}")
print(fun.__code__.co_nlocals)
fun()

