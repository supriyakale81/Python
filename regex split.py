import re
text="""Customer review: 
I really loved the product! Please contact me at john.doe@example.com for more information.
Another customer said: 
The service was excellent. Reach out to jane.smith@email.com if you have any questions."""

r=re.split(r":",text)
print(r)

r1=re.split(r"\s+",text,maxsplit=2)
print(r1)

r1=re.split(r"\s+",text,maxsplit=3)
print(r1)


target_string = "12,45,78,85-17-89"

# use OR (|) operator to combine two pattern
result = re.split(r"-|,", target_string)
print(result)

r1=re.split(r":|@",text)
print(r1)

r1=re.split(r"[:|@|.|\n|,]",text)
print(r1)

# split the string by uppercase words
text="PYTHON is OBJECT ORIENTED proGramMing LANGUAGE"
r2=re.split("[A-Z]+",text)
print(r2)