products = input('Введите товары через запятую: ').split(', ')
index_product = int(input('Позиция для удаления товара: ')) - 1

products.pop(index_product)

print(f'Товары на полке: {", ".join(products)}')