def price_dictionary(key: str) -> None:
    products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
    print(f'Цена: {products.get(key)} руб.')

price_dictionary(input('Введите товар: '))