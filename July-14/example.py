import json

# JSON - JavaScript Object Notation
# data = '{"type": "forecast","duration": 3,"city": "Karaganda","country_code": "kz"}'
#
# request = json.loads(data)
# request['city'] = 'Алматы'
#
# data = json.dumps(request, ensure_ascii=False)
# print(data)

with open('example.txt', encoding='utf-8') as my_file:
    request = json.load(my_file)

request['city'] = 'Hallo'

print(my_file)

with open('example.txt', 'w', encoding='utf-8') as my_file:
    json.dump(request, my_file, ensure_ascii=False)
