config = {}
extended_data = []

cfg_file = open('config.ini', encoding='utf-8')
text = cfg_file.readlines()
cfg_file.close()

current_section = ''

for x in text:
    data = x.split("=")
    data[0] = data[0].strip()
    if len(data) == 1:
        if data[0].startswith('[') and data[0].endswith(']'):
            config[data[0][1:-1]] = {}
            current_section = data[0][1:-1]
    else:
        data[1] = data[1].strip()
        if data[0].startswith('#' or ';'):
            continue
        elif data[1].lower() in ['true', 'yes', 'on']:
            data[1] = True
        elif data[1].lower() in ['false', 'no', 'off']:
            data[1] = False
        elif data[1].isdigit():
            data[1] = int(data[1])
        config[current_section][data[0]] = data[1]
print(config)

