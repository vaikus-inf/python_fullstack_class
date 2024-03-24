class Fountain:
    def spray_water(self) -> str:
        return "Как-то неопределенно брызгает воду"

class SimpleFountain(Fountain):
    def spray_water(self) -> str:
        return "Просто брызгает воду"
    
class MusicalFountain(Fountain):
    def spray_water(self) -> str:
        return "Брызгает воду под музыку"

class LightedFountain(Fountain):
    def spray_water(self) -> str:
        return "Брызгает воду с подсветкой"


fountains = [SimpleFountain(), MusicalFountain(), LightedFountain()]

for item in fountains:
    print(item.spray_water())
