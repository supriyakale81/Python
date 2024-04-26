import re
s="56789 This is a sample sentence with the word 'example' in it. Helllo 1234"

# pattern to find 6 letter word at the begining
res=re.match(r"\w{6}",s)
print(res)
res=re.search(r"\w{6}",s)
print(res.group())
res=re.findall(r"\w{6}",s)
print(res)

# match 6 letter word at the end of the string
res=re.search(r"\w{6}$",s)
print(res)

# match 4 digit number at the end of the string
res=re.search(r"\w{4}$",s)
print(res.group())

res=re.search(r"\d{4}$",s)
print(res.group())


# match 4 digit number at the begining of the string
res=re.search(r"\w{4}",s)
print(res.group())

res=re.search(r"\d{4}",s)
print(res.group())



import re

target_string = "Jessa and Kelly are good friends.Jessa is staying in the hostel and Kelly live near to the college."

# Match five-letter word
res = re.match(r"\b\w{5}\b", target_string)

# printing entire match object
print(res)

# Extract Matching value
print(res.group())


# Start index of a match
print(res.start())


# End index of a match
print("End index: ", res.end())

# Start and end index of a match
pos = res.span()
print(pos)


# Use span to retrieve the matching string
print(target_string[pos[0]:pos[1]])


print("--------------------------------")
# Match any character
S="Hello , I am 23 years old.34567"
r=re.match(r".",S)
print(r.group())

# Match all digits
r=re.findall(r'\d',S)
print(r)

# match all numbers
r=re.findall(r'\d+',S)
print(r)

# Match all special characters and symbols
s1=" Hey,@Sahyadri #Treckcamp $23% &* ^amazing!"
r1=re.findall(r'\W',s1)
print(r1)

print("_____________________________")
S="Hello , I am 23 years old.34567"
r=re.search(r"\d{2}",S)
print(r.group())

print("_____________________________")
S="Hello , I am 23 years old.34567"
r=re.match(r"\d{2}",S)
print(r)

S="Hello , I am 23 years old.34567"
r=re.search(r"\d+",S)
print(r.group())

# Define the target string
text = "Example string to match at the end"

# Define the regex pattern to match at the end of the string
pattern = "end$"

# Using re.fullmatch() to match the pattern at the end of the string
fullmatch = re.fullmatch(pattern, text)
print(fullmatch)

# Using re.match() to match the pattern at the end of the string
match1 = re.match(pattern, text)
print(match1)



