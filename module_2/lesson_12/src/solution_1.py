def collect_data(data: list[int]) -> None:
    def process_data(data: list[int]) -> None:
        def summarize_data(average_value: float) -> None:
            if average_value > int(average_value):
                print(f'Итог: Среднее значение: {average_value}')
            else:
                print(f'Итог: Среднее значение: {int(average_value)}')
        summarize_data(sum(data) / len(data))
    process_data(data)

collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])