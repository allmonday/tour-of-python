import re

sentence = "我很丑，可是我很温柔，但是你怎么看？"
separator = ["可是","但是"]
pattern1 = "(%s)"%('|'.join(separator))
print(pattern1)
print(re.split(pattern1, sentence))
