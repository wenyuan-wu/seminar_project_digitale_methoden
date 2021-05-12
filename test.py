import re
import sacrebleu


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

refs = ['T h e d o g b i t t h e m a n']
sys = 'T h e d o g b i t t h e m a n'
bleu = sacrebleu.sentence_bleu(sys, refs)
bb = sacrebleu.extract_char_ngrams('test', 2)
print(bb)
print(type(bleu.score))
s = "BINGO"
print(" ".join(s))
