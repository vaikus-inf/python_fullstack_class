import json

with open('module_4/lesson_2/src/sales.json', encoding='utf-8') as file:
    data = json.load(file)

revenue_by_category: dict[str, int] = {}

for item in data['sales']:
    if item['category'] in revenue_by_category:
        revenue_by_category[item['category']] += item['total_price']
    else:
        revenue_by_category[item['category']] = item['total_price']

for key, value in revenue_by_category.items():
    print(f'Выручка по категории {key}: {value}')
