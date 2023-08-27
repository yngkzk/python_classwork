import json

try:
    fp = open('inp.json')
except FileNotFoundError:
    print("File not found")
info = json.load(fp)
fp.close()
# print(info)

result = {}
for soldier in info['soldiers']:
    height = soldier['height']
    for size, value in info['sizes'].items():
        if value['from'] < height <= value['to']:
            if size in result:
                result[size] += 1
            else:
                result[size] = 1
print(result)

out = open('out.json', 'w')
json.dump(result, out)
out.close()

soldier_info = info['soldiers'][2]['first_name'] + ' ' + info['soldiers'][2]['last_name']
print(soldier_info)

# sizes = [value['to'] for value in info['sizes'].values()]
sizes = ' '.join(map(lambda x: str(x['to']), info['sizes'].values()))  # в лямбе нужно работать только с (x) в данном случае
print(sizes)

'''
{"xs": 5, "s": 2, "m": 4}
'''
