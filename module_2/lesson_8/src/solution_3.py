def price_dictionary() -> None:
    products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

    min_price = min(products.values())
    max_price = max(products.values())
    
    for key, value in products.items():
        if value == min_price:
            print(f'Самый дешевый: {key} - {value} руб.')
        if value == max_price:
            print(f'Самый дорогой: {key} - {value} руб.')

price_dictionary()