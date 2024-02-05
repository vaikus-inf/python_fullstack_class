def binary_find_element(list_elements: list[int], element: int = 0) -> bool:
    
    while len(list_elements) != 0:
        index_last_element: int = len(list_elements) - 1

        if list_elements[index_last_element // 2] == element:
            return True
        if list_elements[index_last_element // 2] > element:
            list_elements = list_elements[:index_last_element // 2]
        else:
            list_elements = list_elements[index_last_element // 2 + 1:]

    return False


print(binary_find_element([1, 2, 3, 4, 5], 2))
print(binary_find_element([1, 2, 3, 4, 5], 6))
print(binary_find_element([0, 1, 2, 3, 4, 5], 4))
print(binary_find_element([1, 2, 3, 4, 5, 6], 0))
print(binary_find_element([], 5))
