first_list = [1, 2, 5, True, "Hello", "Random word"]
second_list = [2, 5, False, "bye-bye"]
a = first_list.append(6)
print(first_list)

b = first_list.extend(second_list)
print(first_list)

c = first_list.insert(4, "string")
print(first_list)

third_list = [1, 2, 5, True, "cake"]
removed = third_list.remove("cake")
print(third_list)

popped = third_list.pop(3)
print(third_list, popped)

third_list.clear()
print(third_list)

fourth_list = [1, 2, 2, 3, True, "cake", "cake", "World", 1, 2]
find_index = fourth_list.index("World")
print(fourth_list, find_index)

find_similar_elements = fourth_list.count("cake")
print(fourth_list, find_similar_elements)

example_for_sort = ["cake", "world", "rade", "bed", "numbers"]
sorted_list = example_for_sort.sort(reverse=False)
print(example_for_sort)

fifth_list = ["Hello", 666, 0, "sun"]
copy_list = fifth_list.copy()
print(fifth_list, copy_list)

reversed_list = fifth_list.reverse()
print(fifth_list)

print(fifth_list is copy_list)
