def find_max_price(list_price: list = []) -> int:
    if len(list_price) == 0:
        return 'Необходимо передать в функцию список цен!'
    elif len(list_price) == 1:
        return list_price[0]
    else:
        max_price = find_max_price(list_price[1:])
        return max_price if max_price > list_price[0] else list_price[0]

print(find_max_price([15, 7, 9]))
print(find_max_price([1, 10, 20, 5]))
print(find_max_price([25, 25, 25]))
print(find_max_price([10, 8, 12]))