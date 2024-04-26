import re
text="""Customer review: 
I really loved the product! Please contact me at john.doe@example.com for more information.
Another customer said: 
The service was excellent. Reach out to jane.smith@email.com if you have any questions."""

pattern = r'\b[A-Za-z0-9.%+_]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
match = re.findall(pattern, text)
print(match)

# search multiple words

pattern=r"\bexcellent\b|\bproduct\b|\binformation\b"
result=re.findall(pattern,text)
print(result)
# Case insensitive regex search
pattern=r"\bExcellent\b|\bproduCt\b|\binformation\b"
result=re.findall(pattern,text,re.IGNORECASE)
print(result)

#finditer
pattern=r"\bexcellent\b|\bproduct\b|\binformation\b"
result1=re.finditer(pattern,text)
print(result1)
for r in result1:
    print(r.group())
