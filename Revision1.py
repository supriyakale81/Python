class solution:
    def mergealternatively(self,word1,word2):
        m=[]
        i=0
        j=0
        while i <len(word1) or j<len(word2):
            if i<len(word1):
                m.append(word1[i])
                i+=1
            if j < len(word2):
                m.append(word2[j])
                j+=1
        return ''.join(m)

word1 = "hello"
word2 = "world"
c=solution()
merged_string = c.mergealternatively(word1, word2)
print(merged_string)

class solution:
    def greatestdivisor(self,s1,s2):
        if s1+s2!=s2+s1:
            return ""
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
        length = gcd(len(s1), len(s2))
        return s1[:length]
c=solution()
c.greatestdivisor("ABCABC","ABC")



# Extract Unique values dictionary values
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
def unique_values(test_dict):
    l=[]
    for v in test_dict.values():
        for x in v:
            if x not in l:
                l.append(x)
    l.sort()
    print(l)
unique_values(test_dict)

# Python program to find the sum of all items in a dictionary
def sum_values(dict):
    sum=0
    for v in dict.values():
        sum+=v
    print(sum)
sum_values({'a':100,'b':400,'c':300,'d':200})

# Ways to remove a key from dictionary
d={'a':100,'b':400,'c':300,'d':200}
del d['c']
print(d)


def remove_key(d1):
    dict={}
    for k,v in d1.items():
        if k!='c':
            dict[k]=v
    print(dict)
remove_key({'a':100,'b':600,'c':100,'d':200})


import re
def check(str1,pattern):
    if re.search(pattern,str1):
        print()





