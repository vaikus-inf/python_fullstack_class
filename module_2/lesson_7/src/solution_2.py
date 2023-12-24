def sublist_amount(prices: str) -> None:
    prices_to_int = [int(item) for item in prices.split(', ')]
    print(f'Сумма подсписка: {sum(prices_to_int[1:4])}')

sublist_amount('1, 2, 3, 4, 5')
sublist_amount('10, 20, 30')