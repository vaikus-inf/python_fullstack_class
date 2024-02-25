class Temperature:
    
    @staticmethod
    def celsius_to_fahrenheit(degrees_celsius: float) -> float:
        return round(degrees_celsius * 9 / 5 + 32, 1)

    @staticmethod
    def fahrenheit_to_celsius(degrees_fahrenheit: float) -> float:
        return round((degrees_fahrenheit - 32) * 5 / 9, 1)


print(f'Градусов Фаренгейта - {Temperature.celsius_to_fahrenheit(20)}')
print(f'Градусов Цельсия - {Temperature.fahrenheit_to_celsius(73)}')
