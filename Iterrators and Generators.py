def list1(l):
    for x in l:
        print(x)

list1([23,34,56,78,"Riya"])
####### ITERATORS ##########
iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
l1=[23,34,56,78,"Riya"]
l2=iter(l1)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<=5:
            x = self.a
            self.a += 1
            return x
        else:
            StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))

###### GENERATORS ########
# USED yield instead of return
# Generator expression to generate multiples of 5 between 0 and 5 that are divisible by 2
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

# Iterating over the generator object and printing the values
for i in generator_exp:
    print(i)

import docx2txt

file_path = r"C:\Users\Supriya\Downloads\Introduction.docx"
f = docx2txt.process(file_path)
print(f)




