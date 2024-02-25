from datetime import date

class Person:
    population: int = 0
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, date.today().year - birth_year)
        
    @classmethod
    def display_current_population(cls) -> None:
        print(f'Текущая популяция = {cls.population}')
    
    def __str__(self) -> str:
        return f'Имя - {self.name}, полных лет - {self.age}.'


person1 = Person.from_birth_year('Иван', 1990)
print(person1)
person2 = Person('Сергей', 19)
print(person2)
Person.display_current_population()
