'''  Система учёта остатков '''


def update_stock(item: str, quantity: int, stock: dict) -> None:
    '''
    Изменение количества имеющегося на складе товара
    или добавление нового товара
    '''
    if item in stock:
        stock[item]["quantity"] += quantity
    else:
        stock[item] = {"quantity": quantity}


def get_item_quantity(item_name: str, stock: dict) -> int:
    ''' Получение остатков заданного товара '''
    return stock[item_name]["quantity"]


def remove_item(item: str, stock: dict) -> None:
    ''' Удаление заданного товара со склада '''
    if item in stock:
        del stock[item]


stock_dict: dict = {}

update_stock("Apple", 50, stock_dict)
update_stock("Banana", 30, stock_dict)
update_stock("Coffee", 20, stock_dict)

print(get_item_quantity("Apple", stock_dict))

remove_item("Banana", stock_dict)

print(stock_dict)
