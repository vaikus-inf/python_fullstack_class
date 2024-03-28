import csv

with open('clients.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Surname', 'Birthday', 'Bonuses'])

    print('Добрый день!', end=' ')
    while True:
        print('Вводите данные:')
        name = input('Имя: ')
        if name == 'stop':
            break
        surname = input('Фамилия: ')
        birthday = input('День рождения: ')
        bonuses = input('Баланс бонусов: ')

        writer.writerow([name, surname, birthday, bonuses])

        print(f'Спасибо! Клиент {name} добавлен!')
