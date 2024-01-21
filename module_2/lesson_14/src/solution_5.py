from collections import OrderedDict

def product_categories(list_products: list) -> dict[str, int]:
    list_categories: list[str] = list(map(lambda item: item[1], list_products))
    dict_categories: dict[str, int] = dict(OrderedDict.fromkeys(list_categories))
    for key in dict_categories:
        dict_categories[key] = list_categories.count(key)
    return dict_categories

print(product_categories([('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]))
print(product_categories([('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]))
print(product_categories([('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]))