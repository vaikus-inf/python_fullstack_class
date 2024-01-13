def type_checking(func):
    def wrapper(*args):
        if len(list(args)) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
            func(*args)
        else:
            errors: list[str] = []
            if len(list(args)) != 2:
                errors.append('Количество аргументов не равно двум!')
            if not isinstance(args[0], str):
                errors.append('Первый аргумент не строка!')
            if not isinstance(args[1], int):
                errors.append('Второй аргумент не число!')
            print(f'Ошибка: {", ".join(errors)}')
    return wrapper

@type_checking
def estimate_time(*args) -> None:
    print('Estimated time calculated successfully.')

estimate_time('Веб-сайт', 'пять')
estimate_time('Визитка', 10)
estimate_time(1, 'Логотип', 'три')