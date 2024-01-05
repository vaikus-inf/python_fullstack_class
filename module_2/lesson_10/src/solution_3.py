def responsible_employee(employee_dictionary: dict[str, int]) -> str:
    max_value: int = max(employee_dictionary.values())
    list_responsible: list[str] = [item for item in employee_dictionary if employee_dictionary[item] == max_value]
    return ', '.join(list_responsible)

print(f'Самый ответственный: {responsible_employee({"Анна": 5, "Боб": 7, "Сюзан": 9})}')
print(f'Самый ответственный: {responsible_employee({"Джон": 1, "Майк": 1, "Эмили": 1})}')