from datetime import date

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, date.today().year - birth_year)
    
    def __str__(self) -> str:
        return f'Имя - {self.name}, полных лет - {self.age}.'


person1 = Person.from_birth_year('Иван', 1990)
print(person1)
person2 = Person.from_birth_year('Анна', 1972)
print(person2)
