import re


pattern = r',\s*'
text = 'June 24,' \
       ' September 20, ' \
       'August 9, ' \
       'October 10'

result = re.split(pattern, text)
print(result)

pattern = r'([A-Za-z]+ [0-9]{2})'
result = re.sub(pattern, 'SUI', text)

print(result)

