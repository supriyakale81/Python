iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

for item in iterable:
    print(item, end=",")

print("\nIterating on an iterator:")
for item in iterator_obj:
    print(item, end=",")

list1=[23,34,56,78,"Riya"]
I1=iter(list1)
for x in I1:
    print(x)


# Write a Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator.

class products:
    def runninig_product(self,iterator):
        product=1
        for x in iterator:
            product*=x
            yield product
p=products()
c=p.runninig_product([1,2,3,4,5])

for item in c:
    print(item)

# Write a Python program to generate the maximum and minimum values of the elements of an iterable.

class max_min:
    @staticmethod
    def maximum_minimum(*iterator):
        max_value=float('-inf')
        min_value=float('inf')
        for x in iter(iterator):
            if x > max_value:
                max_value = x
            elif x < min_value:
                min_value = x
        return max_value,min_value
c=max_min()
m=c.maximum_minimum(3,5,7,6)
print(m)
print("maximum value : ",m[0])
print("minimum value : ",m[1])

#  Write a Python program to construct an infinite iterator that returns evenly spaced values starting with a specified number and step.

# def infinite_iterator(start, step):
#     x=start
#     while True:
#         yield x
#         x+=step
#
# f=infinite_iterator(10,2)
# print(f)
# for i in f:
#     print(i)

def inf_cycle(iterator):
    n=int(input("enter n : "))
    for x in range(n):
        for y in iter(iterator):
            print(y)

inf_cycle([3,4,5,6])
def inf_cycle(iterator):
    n=int(input("enter n : "))
    for x in range(n):
        for y in iterator:
            print(y)

inf_cycle([3,4,5,6])
# def inf_cycle(iterator):
#     n=int(input("enter n : "))
#     while True:
#         for y in iterator:
#             print(y)
#
# inf_cycle([3,4,5,6])

# Write a Python program to make an iterator that drops elements from the iterable as soon as an element is a positive number.

def drop_iterator(*iterator):
    for x in iterator:
        if x <= 0:
            yield x
d=drop_iterator(-2,3,-4,-5)
for i in d:
    print(i)



