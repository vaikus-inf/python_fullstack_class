prices = input('Введите цены: ').split(', ')
prices_to_int = [int(value) for value in prices]
prices_to_int.sort(reverse=True)
print('Отсортированные цены: ', ', '.join(map(str, prices_to_int)))