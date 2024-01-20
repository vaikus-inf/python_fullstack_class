from collections import OrderedDict

def items_for_sale(list_prices: list[int]) -> list[int]:
    return list(OrderedDict.fromkeys(map(lambda price: round(price, -2), list_prices)))

print(items_for_sale([99, 150, 200, 349, 500]))