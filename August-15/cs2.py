user_in = '6,3,7,2,9,0,8,1'
my_list = user_in.split(',')

my_list = list(map(int, my_list))


def quick_sort(value):
    if len(value) <= 1:
        return value
    pivot = value[0]
    less = list(filter(lambda x: x < pivot, value))
    # less = [x for x in value if x < pivot]
    equals = list(filter(lambda x: x == pivot, value))
    more = list(filter(lambda x: x > pivot, value))
    result = quick_sort(less) + equals + quick_sort(more)
    return result


print(quick_sort(my_list))
