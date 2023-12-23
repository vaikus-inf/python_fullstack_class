prices = input('Введите цены: ').split(', ')
new_prices = [int(value) for value in prices]

min_value = min(new_prices)
max_value = max(new_prices)
min_value_index = new_prices.index(min_value)
max_value_index = new_prices.index(max_value)

new_prices[min_value_index], new_prices[max_value_index] = new_prices[max_value_index], new_prices[min_value_index]

print('Новые цены: ', ', '.join(map(str, new_prices)))