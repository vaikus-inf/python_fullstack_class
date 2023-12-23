prices = input('Введите список: ').split(', ')

prices_to_int = [int(prices[i]) for i in range(len(prices)) if i >= 1 and i <= 3]

print(f'Сумма подсписка: {sum(prices_to_int)}')