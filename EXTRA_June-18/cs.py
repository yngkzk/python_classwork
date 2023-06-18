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

print(ridge_case(nick_1))
print(ridge_case(nick_2))
print(ridge_case(nick_3))