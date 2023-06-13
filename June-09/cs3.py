black = '#'
white = ' '
maxheigh = 0
ord_letter = ord('A')
chr_letter = 64
horz = 0
while maxheigh != 8:
        cell = (black + white) * 8
        chr_letter += 1
        maxheigh += 1
        horz += 1
        print(chr(int(chr_letter)), cell, horz)
while horz != 8:
    horz += 1
    print(horz)