products = input('Введите товары через запятую: ').split(', ')
index_new_product = int(input('Позиция для нового товара: ')) - 1
new_product = input('Введите новый товар: ')

products.insert(index_new_product, new_product)

print(f'Товары на полке: {", ".join(products)}')