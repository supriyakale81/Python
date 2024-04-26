import re

text = "Python is a powerful language"

pattern = r'powerful'

match = re.search(pattern, text)
print(match.group())


text = "The number is 12345"

# Define the regex pattern to search for digits
pattern = r'\d$'

match = re.search(pattern, text)
print(match.group())



text="""Customer review: 
I really loved the product! Please contact me at john.doe@example.com for more information.
Another customer said: 
The service was excellent. Reach out to jane.smith@email.com if you have any questions."""

pattern = r'\b[A-Za-z0-9.%+_]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

match = re.match(pattern, text)
print(match)
text="""Customer review: 
I really loved the prodUCt! Please contact me at john.doe@example.com for more information.
Another customer said: 
The service was excellent. Reach out to jane.smith@email.com if you have any questions."""

pattern = r'\b[A-Za-z0-9.%+_]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

match = re.fullmatch(pattern, text)
print(match)

match = re.search(pattern, text)
print(match)

match = re.findall(pattern, text)
print(match)

# search multiple words

pattern=r"\bexcellent\b|\bproduct\b|\binformation\b"
result=re.search(pattern,text)
print(result.group())
# Case insensitive regex search
pattern=r"\bExcellent\b|\bproduct\b|\binformation\b"
result=re.search(pattern,text,re.IGNORECASE)
print(result.group())

































