def collect_data(data: list[int]) -> None:
    def process_data(data: list[int]) -> None:
        def summarize_data(average_value: float) -> None:
            print(f'Итог: Среднее значение: {average_value}')
        summarize_data(sum(data) / len(data))
    process_data(data)

collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])