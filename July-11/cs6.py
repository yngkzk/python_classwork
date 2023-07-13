my_file = open('input6.txt', encoding='utf-8')
text = my_file.read()
my_file.close()

def top3(st):
    st = st.replace(' ', '')
    top1 = 0
    top1_symb = ''
    top2 = 0
    top2_symb = ''
    top3 = 0
    top3_symb = ''
    for i in range(len(st)):
        quantity = st.count(st[i])
        if quantity > top1:
            top1 = quantity
            top1_symb = st[i]
        else:
            if quantity > top2:
                if quantity == top1:
                    continue
                top2 = quantity
                top2_symb = st[i]
            else:
                if quantity > top3:
                    if quantity == top2:
                        continue
                    top3 = quantity
                    top3_symb = st[i]
    return {top1: top1_symb, top2: top2_symb, top3: top3_symb}

result = top3(text)

key1 = list(result)[0]
val1 = list(result.values())[0]
key2 = list(result)[1]
val2 = list(result.values())[1]
key3 = list(result)[2]
val3 = list(result.values())[2]

message = ' символ ' + str(val1) + ' - встречается ' + str(key1) + ' раз, \n символ ' + str(val2) + ' - встречается ' + str(key2) + ' раз, \n символ ' + str(val3) + ' - встречается ' + str(key3) + ' раз'
print(message)