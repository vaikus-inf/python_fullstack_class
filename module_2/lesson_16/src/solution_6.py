import math


def workspace(size: int) -> list:
    matrix: list = [['X' for j in range(size)] for i in range(size)]
    for i in range(size):
        matrix[0 + i][size - 1 - i] = 5
        matrix[i][i] = 0
    
    for i in range(math.ceil(size / 2) - 1):
        for j in range(1, size - i * 2 - 1):
            matrix[i][j + i] = 1
            matrix[j + i][i] = 2
            matrix[size - 1 - i][j + i] = 3
            matrix[j + i][size - 1 - i] = 4

    return matrix


def print_workspace(matrix: list) -> None:
    print('Схема рабочих мест:')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


print_workspace(workspace(3))
print_workspace(workspace(5))
