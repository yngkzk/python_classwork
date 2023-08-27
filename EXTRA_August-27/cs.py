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

'''
{"xs": 5, "s": 2, "m": 4}
'''
