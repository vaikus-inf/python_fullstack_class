class Animal:
    def __init__(
            self,
            name: str,
            says: str
    ) -> None:
        self.name = name
        self.says = says

    def __str__(self) -> str:
        return f'Это животное - {self.name}!'

    def make_sounds(self) -> str:
        return f'{self.name} говорит "{self.says}"'
    
    def eat(self) -> str:
        return f'{self.name} ест'


cow = Animal('Корова', 'Му')
print(cow)
print(cow.make_sounds())
dog = Animal('Собака', 'Гав')
print(dog)
print(dog.eat())
