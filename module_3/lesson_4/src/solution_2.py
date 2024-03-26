from typing import Protocol

class FileHandler(Protocol):
    def read(self) -> None:
        pass
    
    def write(self, data: str) -> None:
        pass

class TextFileHandler(FileHandler):
    def __init__(self, text_file: str) -> None:
        self.text_file = text_file
    
    def read(self) -> None:
        with open(self.text_file, 'r') as file:
            file_content = file.read()
            print(f'Содержимое текстового файла: {file_content}')
    
    def write(self, data: str) -> None:
        with open(self.text_file, 'w') as file:
            file.write(data)
            print('Текстовый файл успешно записан')

class BinaryFileHandler(FileHandler):
    def __init__(self, binary_file: str) -> None:
        self.binary_file = binary_file
        
    def read(self) -> None:
        with open(self.binary_file, 'rb') as file:
            file_content = file.read()
            print(f'Содержимое бинарного файла: {file_content}')
    
    def write(self, data: str) -> None:
        with open(self.binary_file, 'wb') as file:
            file.write(data.encode())
            print('Бинарный файл успешно записан')

def save_data(handler: FileHandler, data: str) -> None:
    handler.write(data)
    handler.read()


text = TextFileHandler('text_file.txt')
binary = BinaryFileHandler('binary_file.bin')
save_data(text, 'Это текст для проверки работы программы')
save_data(binary, 'Это текст для проверки работы программы')
