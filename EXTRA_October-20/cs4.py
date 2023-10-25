import re
import datetime


with open('book.txt', encoding='utf-8') as file:
    text = file.read()


pattern = r'([0-9]{2}[.-]{1}[0-9]{2}[.-]{1}[0-9]{4})'
result = re.findall(pattern, text)

time_delta = datetime.timedelta(days=13)

for start_date in result:
    if start_date[2] == '.':
        date_str = datetime.datetime.strptime(start_date, '%d.%m.%Y')
    else:
        date_str = datetime.datetime.strptime(start_date, '%d-%m-%Y')
    differentTime = date_str - time_delta
    diffString = differentTime.strftime('%d/%m/%Y')
    print(diffString)
    
    text = text.replace(start_date, diffString)
    print(text)

with open('book.txt', 'w', encoding='utf-8') as file:
    file.write(text)
