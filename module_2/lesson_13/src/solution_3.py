cached_results: list = []

def caching(func):
    def wrapper(*args):
        if list(args) not in cached_results:
            func('Посчитали цену: 3000')
            cached_results.append(list(args))
        else:
            func('Загрузили из кеша: 3000')
    return wrapper

@caching
def calculate_project_cost(text) -> None:
    print(text)

calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost('Логотип', 'малый бизнес')