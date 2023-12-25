def synonyms_in_design(word: str) -> None:
    synonyms: dict[str, int] = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
    
    if word in synonyms:
        print(f'Синоним: {synonyms[word]}')
    else:
        condition = input('Введенное слово отсутствует в словаре! Хотите добавить это слово и его синоним в словарь? (Да/Нет): ')
        if condition == 'Да':
            synonym = input(f'Введите синоним к слову {word}: ')
            synonyms[word] = synonym
            print(f'Синоним: {synonyms[word]}')
        else:
            print('До свидания!')

synonyms_in_design(input('Введите слово: '))