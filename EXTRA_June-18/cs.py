def ridge_case(NiCkNaMe):
    index = 0
    result = ""
    for char in NiCkNaMe:
        if index % 2:
            result += char.lower()
        else:
            result += char.upper()
        index += 1
    return result

nick_1 = ridge_case("hellosup")
nick_2 = ridge_case("dsanaaa")
nick_3 = ridge_case("ykzkzs")

print(nick_1)
print(nick_2)
print(nick_3)