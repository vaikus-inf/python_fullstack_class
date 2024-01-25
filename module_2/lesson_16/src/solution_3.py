def shelves_for_goods(shelf_list: list) -> list:
    return [[item[1] * (i + 1)] * item[1] for i, item in enumerate(shelf_list)]
    

print(f'Скидки: {shelves_for_goods([[4, 2], [5, 3], [6, 5]])}')
print(f'Скидки: {shelves_for_goods([[3, 1], [4, 4]])}')
