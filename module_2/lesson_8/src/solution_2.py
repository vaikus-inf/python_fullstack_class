dictionary_synonyms: dict[str, int] = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}

def synonyms_in_design(synonyms, word: str) -> None:
        
    if word in synonyms:
        print(f'Синоним: {synonyms[word]}')
    elif word in synonyms.values():
        synonyms_values_arr = list(synonyms.values())
        synonyms_keys_arr = list(synonyms.keys())
        print(f'Синоним: {synonyms_keys_arr[synonyms_values_arr.index(word)]}')
    else:
        condition = input('Введенное слово отсутствует в словаре! Хотите добавить это слово и его синоним в словарь? (Да/Нет): ')
        if condition == 'Да':
            synonym = input(f'Введите синоним к слову {word}: ')
            synonyms[word] = synonym
            print(f'Синоним: {synonyms[word]}')
        else:
            print('До свидания!')

synonyms_in_design(dictionary_synonyms, 'Красивый')
synonyms_in_design(dictionary_synonyms, 'Прекрасный')
synonyms_in_design(dictionary_synonyms, 'Яркий')