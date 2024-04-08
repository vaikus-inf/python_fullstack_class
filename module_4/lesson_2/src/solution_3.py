import csv, json, copy, re
from datetime import datetime, date

class Client:
    def __init__(self, name, surname, birthday, bonuses) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    def data_verification(self):
        if not re.match(r'^[а-яА-ЯёЁ]+$', self.name) or not re.match(r'^[а-яА-ЯёЁ]+$', self.surname):
            return False
        
        if 0 > self.bonuses > 10000000 or not isinstance(self.bonuses):
            return False
        
        bd = datetime.strptime(self.birthday, "%d.%m.%Y").date()
        if bd < date(1950, 1, 1) or bd > date.today():
            return False

clients_dict: dict[str, list] = {'clients': []}

with open('module_4/lesson_2/src/clients.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for i, row in enumerate(reader):
        if i == 0:
            keys: list[str] = copy.deepcopy(row)
        else:
            clients_dict['clients'].append({
                keys[0]: row[0],
                keys[1]: row[1],
                keys[2]: row[2],
                keys[3]: row[3]
            })

print(clients_dict)

with open('module_4/lesson_2/src/clients.json', 'w', encoding='utf-8') as json_file:
    json.dump(clients_dict, json_file)
