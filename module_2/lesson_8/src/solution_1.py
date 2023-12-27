def price_dictionary(key: str) -> None:
    products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
    
    if key in products:
        print(f'Цена: {products[key]} руб.')
    else:
        print('Введенный товар отсутствует в словаре!')

price_dictionary('Яблоко')
price_dictionary('Кофе')