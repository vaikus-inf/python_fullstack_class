products = input('Введите товары через запятую: ').split(', ')
print('Товары с нечетными индексами: ', ', '.join(products[1::2]))