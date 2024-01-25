def shelves_for_goods(shelf_lengths: str, number_of_products: str) -> list:
    return [[int(length), int(products)] for length, products in zip(shelf_lengths.split(', '), number_of_products.split(', '))]


print(f'Полки: {shelves_for_goods("4, 5, 6", "2, 3, 5")}')
print(f'Полки: {shelves_for_goods("3, 4", "1, 4")}')
