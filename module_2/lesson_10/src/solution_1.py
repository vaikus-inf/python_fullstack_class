def discounts_for_customers(price: int = 0, visits: int = 0) -> int:
    if 10 <= visits < 20:
        return round(price - price * 10 / 100)
    elif visits >= 20:
        return round(price - price * 20 / 100)
    return price
    
print(f'Итоговая цена: {discounts_for_customers(100, 5)}')
print(f'Итоговая цена: {discounts_for_customers(200, 10)}')
print(f'Итоговая цена: {discounts_for_customers(150, 20)}')