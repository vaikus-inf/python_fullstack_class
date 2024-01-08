def sales_schedule_with_range(number_of_days: int = 0) -> None:
    print(f'Дни распродаж: {list(range(3, number_of_days + 1, 3))}')

sales_schedule_with_range(30)
sales_schedule_with_range(31)