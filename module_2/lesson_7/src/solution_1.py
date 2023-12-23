original_line = input('Введите строку: ').split(' ')
modified_line = ' '.join([item[::-1] for item in original_line])
print(modified_line)