# Функция возвращает результат деления большего по модулю числа на меньшее.
def smart_div(num1, num2=1):
    if num1 >= num2:
        if num1 > 0:
            if num2 > 0:
                result = num1 / num2
                return result
            else:
                num2 = num2 * -1
                if num1 >= num2:
                    result = num1 / num2
                    return result
                else:
                    result = num2 * -1 / num1
                    return result
        else:
            num1 = num1 * -1
            if num1 >= num2:
                result = num1 / num2
                return result
            else:
                result = num1 * -1 / num2
                return result
    elif num2 == 1:
        return 1
    else:
        if num1 > 0:
            if num2 > 0:
                result = num1 / num2
                return result
            else:
                num2 = num2 * -1
                if num1 >= num2:
                    result = num1 / num2
                    return result
                else:
                    result = num2 * -1 / num1
                    return result
        else:
            num1 = num1 * -1
            if num1 >= num2:
                result = num1 / num2
                return result
            else:
                result = num1 * -1 / num2
                return result





def test_smart_div():
    assert smart_div(20, 4) ==  5
    assert smart_div(3, -6) == -2
    assert smart_div(-8)    ==  1
    
test_smart_div()