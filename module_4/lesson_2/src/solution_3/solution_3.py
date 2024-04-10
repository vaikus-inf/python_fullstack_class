import csv, json, re
from datetime import datetime, date

class Client:
    def __init__(self, name: str, surname: str, birthday: str, bonuses: str) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    @staticmethod
    def name_verification(name: str, surname: str) -> bool:
        if not re.match(r'^[а-яА-ЯёЁ]+$', name) or not re.match(r'^[а-яА-ЯёЁ]+$', surname):
            return False
        return True
    
    @staticmethod
    def birthday_verification(birthday: str) -> bool:    
        birthday_date_type: date = datetime.strptime(birthday, "%d.%m.%Y").date()
        if not (date(1950, 1, 1) <= birthday_date_type <= date.today()):
            return False
        return True
    
    @staticmethod
    def bonuses_verification(bonuses: str) -> bool:    
        try:
            if not (0 <= int(bonuses) <= 10000000):
                return False
        except ValueError:
            return False
        return True

processed_clients: int = 0
missed_clients: int = 0
clients_dict: dict[str, list[dict]] = {'clients': []}

with open('clients.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for i, row in enumerate(reader):
        if i > 0:
            if Client.name_verification(row[0], row[1]) and Client.birthday_verification(row[2]) and Client.bonuses_verification(row[3]):
                clients_dict['clients'].append({
                    'name': row[0],
                    'surname': row[1],
                    'birthday': row[2],
                    'Bonuses': int(row[3])
                })
                processed_clients += 1
            else:
                missed_clients += 1

with open('clients.json', 'w', encoding='utf-8') as json_file:
    json.dump(clients_dict, json_file, ensure_ascii=False, indent=2)

print(f'Было обработано(клиентов): {processed_clients}')
print(f'Было пропущено(клиентов): {missed_clients}')

