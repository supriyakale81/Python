import re
text="PYTHON is OBJECT ORIENTED proGramMing LANGUAGE"
#replace white spaces with hyphen
r2=re.sub(r"\s",'-',text)
print(r2)

# remove all whitespaces
print(re.sub(r"\s","",text))

text="         PYTHON is OBJECT ORIENTED proGramMing LANGUAGE"
print(len(text))
print(re.sub(r"^\s","",text)) # it removes only single space at begining
print(re.sub(r"^\s+","",text))  # removes all whitespaces at the begining
print(len(re.sub(r"^\s+","",text)))
print("------------------------------------")
text="PYTHON is OBJECT ORIENTED proGramMing LANGUAGE   "
print(len(text))
print(len(re.sub(r"\s+$","",text)))
print(re.sub(r"\s+$","",text))
print("------------------------------------")
text="        PYTHON is OBJECT ORIENTED proGramMing LANGUAGE     "
print(len(text))
print(len(re.sub(r"^\s+|\s+$","",text)))
print(re.sub(r"^\s+|\s+$","",text))

target_string = "Emma loves PINEAPPLE, COCONUT, BANANA ice cream"
result = re.subn(r"[A-Z]{2,}", "MANGO", target_string)
print(result)


text = "apple orange apple banana apple"
pattern = r"apple"
replacement = "fruit"

new_text, num_replacements = re.subn(pattern, replacement, text)

print(new_text)
print(num_replacements)

# use re.subn() to replace multiple substrings in a string

str1 = "Hi, my number is 08999XX. I am 23 years old. I live in 221B Baker Street."

str1, n = re.subn('[0-9]', 'X',str1)
print(str1)
print(n)



# Given String
text = "Hi, my number is 08999XX. I am 23 years old. I live in 221B Baker Street."

# Dictionary of substrings to replace
substitutions = {
    '08999XX': 'XXXXX',
    '23': 'twenty-three',
    '221B': '221B Sherlock Holmes'
}

# Iterate over the dictionary items and replace substrings
for old_str, new_str in substitutions.items():
    text, num_replacements = re.subn(re.escape(old_str), new_str, text)

# Output
print(text)  # Updated string after replacing multiple substrings
print(num_replacements)  # Total number of replacements made