import re


pattern = r'\w[\w\.-_]+@[\w][\w\.-_]+\.\w{2,3}'

text = 'Email addresses: .john.doe@example.com,' \
       'jane_smith@example.co.uk'

matches = re.findall(pattern, text)
print(matches)
