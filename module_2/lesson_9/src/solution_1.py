def calculate_discount(*args, discount_percentage) -> float:
    return round(discount_percentage * sum(args) / 100, 2)

print(f'Сумма скидки: {calculate_discount(100, 200, 300, discount_percentage = 10)}')
print(f'Сумма скидки: {calculate_discount(50, 150, 250, discount_percentage = 20)}')