prices = input('Введите цены: ').split(', ')
print('Цены без скидки: ', ', '.join(prices[1::2]))