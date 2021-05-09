import re

text = "341."
pattern = r"\([0-9]{4}\)"

res = re.findall(pattern, text)

print(res)

mystring = "th-is is"

mystring = re.sub(r'[^A-Za-z0-9-]+', '', mystring)

print(mystring)

a = [['azvoger', 'io', '1732'], ['azvoger', 'azvogueryou', '1931']]
b = [['azvogeria', 'azvoguerya', '1732']]
c = [['azvur', 'io', '1732'], ['azvur', 'azvuryou', '1931']]

a = a + b
print(a)
