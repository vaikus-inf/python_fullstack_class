def personnel_management() -> None:
    list_employee: dict[str, dict[str, str]] = {}

    for i in range(6):
        employee = input('Введите (через запятую) Отдел, Должность и Фамилию сотрудника: ').split(', ')
        if employee[0] not in list_employee:
            list_employee[employee[0]] = {}
        list_employee[employee[0]][employee[1]] = employee[2]

    print(f'Снабжение: {list_employee["Снабжение"]}')
    print(f'Дизайн: {list_employee["Дизайн"]}')

personnel_management()