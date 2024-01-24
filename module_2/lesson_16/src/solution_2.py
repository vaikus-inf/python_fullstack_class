def shelves_for_goods(shelf_number: str, number_of_products: str) -> list:
    return [[int(self), int(products)] for self, products in zip(shelf_number.split(', '), number_of_products.split(', '))]


print(f'Полки: {shelves_for_goods("4, 5, 6", "2, 3, 5")}')
print(f'Полки: {shelves_for_goods("3, 4", "1, 4")}')
