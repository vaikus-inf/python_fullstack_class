price_dollars = float(input('Введите цену товара в долларах: '))
exchange_rate = float(input('Введите текущий курс доллара: '))

price_rubles = price_dollars * exchange_rate
print(f'Цена в рублях = {price_rubles}')
