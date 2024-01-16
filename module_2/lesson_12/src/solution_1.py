import statistics

def collect_data(data: list[int]) -> None:
    def process_data(data: list[int]) -> None:
        def summarize_data(average_value) -> None:
            print(f'Итог: Среднее значение: {average_value}')
        summarize_data(statistics.mean(data))
    process_data(data)

collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])