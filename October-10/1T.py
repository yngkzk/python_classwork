import sys
import re


with open(sys.argv[1], encoding='utf-8') as data_file:
    text = data_file.read().split()

pattern = r'\w[\w\.-_]+\w@[\w][\w\.-_]+\.[A-Za-z]{2,3}'
for email in text:
    matches = re.search(pattern, email)
    if not matches:
        print(email)

