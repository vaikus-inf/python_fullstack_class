prices = input('Введите список: ').split(', ')

prices_to_int = [int(item) for item in prices]
n = prices_to_int[0]
m = prices_to_int[-1]
k = prices_to_int[1]

print(f'Числа подсписка: {", ".join(prices[n:m:k])}')