data = ['Снабжение, Менеджер, Иванов',
        'Дизайн, Дизайнер, Смирнов',
        'Снабжение, Менеджер, Петров',
        'Дизайн, Иллюстратор, Cидоров',
        'Маркетинг, Аналитик, Сергеев',
        'Дизайн, Дизайнер, Васильев']

def personnel_management(employee_data) -> None:
    list_employee: dict[str, dict[str, str]] = {}

    for item in employee_data:
        employee = item.split(', ')
        if employee[0] not in list_employee:
            list_employee[employee[0]] = {}
        list_employee[employee[0]][employee[1]] = employee[2]

    print(f'Снабжение: {list_employee["Снабжение"]}')
    print(f'Дизайн: {list_employee["Дизайн"]}')

personnel_management(data)