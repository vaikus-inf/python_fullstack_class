class Book:
    def __init__(
            self,
            title: str,
            author: str
    ) -> None:
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        return f'Название книги - {self.title}, Автор книги - {self.author}'

class Library:
    def __init__(self) -> None:
        self.list_books = []

    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.list_books.append(book)
        return self

    def remove_book(self, title: str):
        for book in self.list_books:
            if book.title == title:
                self.list_books.remove(book)
        return self

    def __getitem__(self, index):
        books = self.list_books[index]
        if isinstance(books, list):
            return [book.__str__() for book in books]
        return books
    
    def __contains__(self, title: str) -> str:
        for book in self.list_books:
            if book.title == title:
                return f'В библиотеке есть книга "{title}"'
        return f'В библиотеке нет книги "{title}"'


home_library = Library()

home_library.add_book('Гарри Поттер', 'Джоан Роулинг').add_book('Мертвые души', 'Николай Гоголь').remove_book('Гарри Поттер').add_book('Каштанка', 'Антон Чехов')

print(home_library[0])
print(home_library[:])

print(home_library.__contains__('Каштанка'))
print(home_library.__contains__('Гарри Поттер'))
