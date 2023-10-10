import re


pattern = r'(?P<month>[A-Za-z]+) (?P<day>\d+) *$'
text = 'June 24, September 20, August 9, October 10'

matched = re.search(pattern, text)
if matched:
    print('0th group - ', matched.group(0), sep='')
    print('1st group - ', matched.group('month'), sep='')
    print('2nd group - ', matched.group('day'), sep='')
