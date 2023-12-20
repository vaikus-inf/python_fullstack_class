products = input('Введите товары: ').split(', ')
index_products = input('Позиции для перестановки: ').split(', ')
index_products_to_int = [int(value) - 1 for value in index_products]

products[index_products_to_int[0]], products[index_products_to_int[1]] = products[index_products_to_int[1]], products[index_products_to_int[0]]

print(f'На полке: {", ".join(products)}')