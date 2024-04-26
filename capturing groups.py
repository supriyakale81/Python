import re

target_string = "The price of PINEAPPLE ice cream is 20"

# two groups enclosed in separate ( and ) bracket
result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)

# Extract matching values of all groups
print(result.groups())

# Extract match value of group 1
print(result.group(1))

# Extract match value of group 2
print(result.group(2))


# Given String
text = "John.7200_24.6.txt.gz"

# Define the regex pattern with capturing groups
pattern = r'^(\w+)\.(\d+)_(\d+)\.(\d+)\.\w+\.gz$'

# Search for the pattern in the text
match = re.search(pattern, text)
print(match.groups())

import re

target_string = "The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 40"

# two groups enclosed in separate ( and ) bracket
# group 1: find all uppercase letter
# group 2: find all numbers
# you can compile a pattern or directly pass to the finditer() method
pattern = re.compile(r"(\b[A-Z]+\b).(\b\d+\b)")
result=re.finditer(pattern,target_string)
# print(result)
# find all matches to groups
for match in result:
    # extract words
    print(match.groups())

print("---------------")
result=re.finditer(pattern,target_string)
for match in result:
    # extract words
    print(match.group(1))
    # extract numbers
    print(match.group(2))

print("---------------")
# Extract Range of Groups Matches
result=re.finditer(pattern,target_string)
for match in result:
    # extract words
    print(match.group(1,2))
print("**---------------**")
# Extract Range of Groups Matches
result=re.search(pattern,target_string)
print(result.group(1,2))
print("**---------------**")
result=re.findall(pattern,target_string)
print(result)

target_string = "abcde25"

result = re.findall(r"[^abc]", target_string)
print(result)


# match any character except digits
result = re.findall(r"[^0-9]", target_string)
print(result)


#  re.I
# re.IGNORECASE
target_str = "KELLy is a Python developer at a PYnative. kelly loves ML and AI"

# Without using re.I
result = re.findall(r"kelly", target_str)
print(result)


# with re.I
result = re.findall(r"kelly", target_str, re.I)
print(result)


# with re.IGNORECASE
result = re.findall(r"kelly", target_str, re.IGNORECASE)
print(result)

