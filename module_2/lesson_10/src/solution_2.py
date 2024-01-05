def background_color(current_time: int = 0) -> str:
    if 0 < current_time > 23:
        return 'Невозможно определить время суток. Укажите корректное время!'
    elif 6 <= current_time <= 18:
        return 'Светлый'
    return 'Темный'

print(f'Цвет фона: {background_color(10)}')
print(f'Цвет фона: {background_color(20)}')
print(f'Цвет фона: {background_color(5)}')