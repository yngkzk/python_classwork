import sys
import json


args_dict = {'text': 'programFile.txt', 'debuglevel': 'debug', 'mode': 'delayed', 'output': 'stdout'}


def parse(arg):
    global args_dict
    for i in range(len(arg)-1):
        match arg[i]:
            case x if x in ('--text', '-t'):
                args_dict['text'] = arg[i+1]
            case j if j in ('--debuglevel', '-d'):
                args_dict['debuglevel'] = arg[i+1]
            case y if y in ('--mode', '-m'):
                args_dict['mode'] = arg[i+1]
            case z if z in ('--output', '-o'):
                args_dict['output'] = arg[i+1]
    return args_dict

def parseFromConfig(file):
    with open(file, encoding='utf-8') as File:
        text = json.load(File)
    for _ in range(len(text)):
        if 'text' in text:
            args_dict['text'] = text['text']
        if 'debuglevel' in text:
            args_dict['debuglevel'] = text['debuglevel']
    return text


print(args_dict)
print(parseFromConfig('config.json'))
print(parse(sys.argv))