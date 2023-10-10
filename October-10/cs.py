import re

pattern = r"apple"
text = "I have an apple. The apple is red."
matched = re.search(pattern, text)
print('Found it - ', matched.group(), sep='')

matches = re.findall(pattern, text)
print('Found it, again... - ', matches, sep='')
