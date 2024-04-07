import json

with open('module_4/lesson_2/src/inventory.json', encoding='utf-8') as file:
    data = json.load(file)

list_materials: list = [dict_item['item'] + ' ' + str(dict_item['minimum_required'] - dict_item['quantity']) + ' шт.'
                        for dict_item in data['inventory'] if dict_item['quantity'] < dict_item['minimum_required']]

print('Необходимо закупить: ', end='')
print(*list_materials, sep=', ')
