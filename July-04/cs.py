number = '321'
answer = number.isnumeric()
print(answer)

name = 'шубадуба'

a = name.find('аду', 0, 2)
a = name.index('дуб', 0, 7)

a = name.lower()
a = name.casefold()

a = name.replace('дуб', 'береза')

a = name.rjust(30, '-')
a = name.ljust(49, '-')
a = name.center(30, '-')
print(a)
