def bracket_balance(character_set: str) -> bool:
    dict_character: dict[str, str] = {'{': 'opening', '(': 'opening', '[': 'opening', '}': '{', ')': '(', ']': '[',}
    list_character: list[str] = []

    for char in character_set:
        if dict_character[char] == 'opening':
            list_character.append(char)
        else:
            if dict_character[char] in list_character and list_character[len(list_character) - 1] == dict_character[char]:
                list_character.pop()
            else:
                return False
    
    return not len(list_character)


print(bracket_balance('{([])}'))
print(bracket_balance('[(])'))
print(bracket_balance('{'))
print(bracket_balance('[]['))
print(bracket_balance(')('))
