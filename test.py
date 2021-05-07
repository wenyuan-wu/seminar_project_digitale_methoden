import re

text = "341."
pattern = r"\([0-9]{4}\)"

res = re.findall(pattern, text)

print(res)

mystring = "th-is is"

mystring = re.sub(r'[^A-Za-z0-9-]+', '', mystring)

print(mystring)
