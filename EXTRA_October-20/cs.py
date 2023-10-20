import sys


def parse(arg):
    args_dict = {}
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

print(sys.argv)
parsed_text = parse(sys.argv)
print(parsed_text)