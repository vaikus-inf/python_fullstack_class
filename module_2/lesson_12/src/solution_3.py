data_sets = [
    ([10, 23, 35, 47], lambda item: item % 2 != 0),
    ([5, 7, 8, 10], lambda item: item > 7),
    ([1, 2, 3, 5, 6], lambda item: item < 5),
    ([10, 20, 30, 40, 50], lambda item: item % 5 == 0 and item % 8 == 0)
]

def filter_data(data: list[int], filter_func) -> list:
    return list(filter(filter_func, data))

for data, filter_func in data_sets:
    filtered_data = filter_data(data, filter_func)
    print(f'Отфильтрованные данные: {filtered_data}')