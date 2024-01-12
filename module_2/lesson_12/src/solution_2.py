order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

def check_order(order: dict) -> bool:
    return bool(order.get('items'))

def package_order(order: dict) -> str:
    return f'Упакован заказ {order["id"]}'

def send_order(check_func, package_func, order) -> str:
    if check_func(order): 
        return f'Отправка: {package_func(order)}'
    else:
        return f'Отправка: Заказ {order["id"]} пуст'

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))