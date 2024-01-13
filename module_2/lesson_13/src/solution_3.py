cached_results: list = []

def caching(func):
    def wrapper(*args):
        func(*args)
        if list(args) not in cached_results:
            cached_results.append(list(args))
    return wrapper

@caching
def calculate_project_cost(*args) -> None:
    if list(args) not in cached_results:
        print('Посчитали цену: 3000')
    else:
        print('Загрузили из кеша: 3000')

calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost('Логотип', 'малый бизнес')