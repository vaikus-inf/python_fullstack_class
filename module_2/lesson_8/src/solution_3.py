def price_dictionary() -> None:
    products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

    price_list = list(products.values())
    min_price = min(price_list)
    max_price = max(price_list)
    
    for key, value in products.items():
        if value == min_price:
            print(f'Самый дешевый: {key} - {value} руб.')
        if value == max_price:
            print(f'Самый дорогой: {key} - {value} руб.')

price_dictionary()