def find_element(list_elements: list, value) -> bool:
    for element in list_elements:
        if element == value:
            return True
    return False


print(find_element([1, 2, 3], 2))
print(find_element(['1', '2', '3'], 2))