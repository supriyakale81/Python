import re
print("without raw string:")
# path_to_search = "c:\example\task\new"
target_string = r"c:\example\task\new\exercises\session1"
# regex pattern
pattern =r"^c:\\example\\task\\new"
res = re.search(pattern, target_string)
print(res.group())

# pattern to find 7 letter word
pattern=re.compile(r"\b\w{7}\b")
res=pattern.findall("Hello, Welcome to the team !!")
print(res)
# pattern to find three consecutive digits
s1="Hello 234 453 567 world 345 45 wow"
p=re.compile(r'\d{3}')
new1=p.findall(s1)
print(new1)

s2= "Welcome to the team 345 568"
new2=p.findall(s2)
print(new2)






