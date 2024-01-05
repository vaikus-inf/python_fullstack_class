def calculate_discount(list_price: list = [], index: int = -1) -> list:  
    if index == -len(list_price):
        return list_price
    else:
        list_price[index] = round(list_price[index] - list_price[index - 1] * 0.1)
        calculate_discount(list_price, index - 1)
    return list_price

print(*calculate_discount([1000, 2000, 3000]), sep=', ')
print(*calculate_discount([5000, 10000, 15000]), sep=', ')
print(*calculate_discount([100, 200, 300, 400]), sep=', ')
print(*calculate_discount([50, 100]), sep=', ')