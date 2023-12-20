prices = input('Введите цены: ').split(', ')
prices_to_int = [int(value) for value in prices]

print(f'Средняя цена товаров: {str(sum(prices_to_int) // len(prices_to_int))}')