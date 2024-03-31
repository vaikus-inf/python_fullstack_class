first_file = ''
last_file = ''

while not first_file[:first_file.find('.')].isdigit() or first_file.find('.') == -1:
    first_file = input('Введите название первого файла: ')
    if not first_file[:first_file.find('.')].isdigit():
        print('Ошибка! Имя файла должно состоять только из цифр.')
    if first_file.find('.') == -1:
        print('Ошибка! Полное имя файла должно состоять из имени и расширения разделенных точкой.')

while not last_file[:last_file.find('.')].isdigit() or last_file.find('.') == -1:
    last_file = input('Введите название последнего файла: ')
    if not last_file[:last_file.find('.')].isdigit():
        print('Ошибка! Имя файла должно состоять только из цифр.')
    if last_file.find('.') == -1:
        print('Ошибка! Полное имя файла должно состоять из имени и расширения разделенных точкой.')

name_first_file = int(first_file[:first_file.find('.')])
name_last_file = int(last_file[:last_file.find('.')])

#Создание файлов, для проверки работы программы
for i in range(name_first_file, name_last_file + 1):
    with open(str(i)+'.txt', 'w', encoding='utf8') as file:
        file.write(f'Тестовый текст для файла {str(i)}.txt')

with open('for_buh.txt', 'w', encoding='utf8') as file_for_buh:
    for i in range(name_first_file, name_last_file + 1):
        with open(str(i)+'.txt', 'r') as payment_information:
            file_content = payment_information.read()
        file_for_buh.write(file_content + '\n')

print(f'Файлы успешно обработаны! Всего {name_last_file - name_first_file + 1} шт.')
