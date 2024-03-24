class Greenhouse:
    def __init__(self, temperature: float = 23.0, moisture_content: int = 45, light_level: int = 180) -> None:
        self._temperature = temperature
        self._moisture_content = moisture_content
        self._light_level = light_level
    
    @property
    def temperature(self) -> float:
        return self._temperature
    
    @temperature.setter
    def temperature(self, value: float) -> None:
        if value < 15 or value > 30:
            raise ValueError("Устанавливаемая температура должна быть между 15-ю и 30-ю градусами Цельсия")
        self._temperature = value
    
    @property
    def moisture_content(self) -> int:
        return self._moisture_content
    
    @moisture_content.setter
    def moisture_content(self, value: int) -> None:
        if value < 30 or value > 65:
            raise ValueError("Устанавливаемая влажность должна быть между 30-ю и 65-ю процентами")
        self._moisture_content = value
    
    @property
    def light_level(self) -> int:
        return self._light_level
    
    @light_level.setter
    def light_level(self, value: int) -> None:
        if value < 150 or value > 300:
            raise ValueError("Устанавливаемый уровень освещенности должен быть между 150-ю и 300-ми люкс")
        self._light_level = value
    

house = Greenhouse(20.0, 50, 200)

print(house.temperature)
house.temperature = 25.5
print(house.temperature)

print(house.moisture_content)
house.moisture_content = 35
print(house.moisture_content)

print(house.light_level)
house.light_level = 150
print(house.light_level)
