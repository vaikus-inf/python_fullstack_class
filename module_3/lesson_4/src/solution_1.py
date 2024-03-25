from abc import ABC, abstractmethod

class Instrument(ABC):    
    @abstractmethod
    def play(self) -> str:
        pass

class Guitar(Instrument):
    def play(self) -> str:
        return "Звучит гитара"

class Piano(Instrument):
    def play(self) -> str:
        return "Звучит пианино"

class Flute(Instrument):
    def play(self) -> str:
        return "Звучит флейта"


instruments: list[Instrument] = [Guitar(), Piano(), Flute()]

for item in instruments:
    print(item.play())
