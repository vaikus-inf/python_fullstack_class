"""CRM-система для магазина"""


def add_client(name: str, history: dict) -> None:
    """Добавление клиента"""
    client_id: int = len(history) + 1
    history[client_id] = {'name': name, 'orders': []}


def make_order(client_id: int, history: dict, order_details: dict) -> None:
    """Создание заказа"""
    history[client_id]['orders'].append(order_details)


def get_history(client_id: int, history: dict) -> list[dict]:
    """Получение истории заказов клиента"""
    return history[client_id]['orders']


client_history: dict = {}

add_client('Roman', client_history)
make_order(1, client_history, {'order_id': 1, 'amount': 100})
print(get_history(1, client_history))
