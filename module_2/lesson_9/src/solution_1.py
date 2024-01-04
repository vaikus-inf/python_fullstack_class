def calculate_discount(*args) -> int:
    return round(args[-1] * sum(args[:-1]) / 100)

print(f'Сумма скидки: {calculate_discount(100, 200, 300, 10)}')
print(f'Сумма скидки: {calculate_discount(50, 150, 250, 20)}')