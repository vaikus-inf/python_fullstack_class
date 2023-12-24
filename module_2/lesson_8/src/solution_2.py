def synonyms_in_design(key: str) -> None:
    synonyms: dict[str, int] = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий', 'Яркий': 'Эффектный'}
    print(f'Синоним: {synonyms.get(key)}')

synonyms_in_design(input('Введите слово: '))