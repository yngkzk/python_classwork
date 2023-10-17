def read_large_file(file):
    with open(file, encoding='utf-8') as myFile:
        for line in myFile:
            yield line

def process_line(line):
    print(line)

for line in read_large_file("bit_data.txt"):
    process_line(line)