import csv, json

with open('module_4/lesson_2/src/clients.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

clients_dict = {
    'clients': [
        {
            'name': row[0],
            'surname': row[1],
            'birthday': row[2],
            'Bonuses': row[3]
        }
    ]
}

print(clients_dict)

with open('module_4/lesson_2/src/clients.json', 'w', encoding='utf-8') as json_file:
    json.dump(clients_dict, json_file)
