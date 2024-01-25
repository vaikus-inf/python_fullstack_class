def spiral_matrix(width: int) -> list:
    matrix: list[int] = [[0 for j in range(width)] for i in range(width)] 
    values: list[int] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x = y = current = 0
    
    for i in range(width * width):
        if x + values[current][0] == width or y + values[current][1] == width or matrix[x + values[current][0]][y + values[current][1]]:
            current = 0 if current == 3 else current + 1
        matrix[x][y] = i + 1
        x += values[current][0]
        y += values[current][1]

    return matrix


def print_spiral_matrix(matrix: list) -> None:
    cell_width: int = len(str((len(matrix) ** 2))) + 1
    print('Матрица проектов:')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(str(matrix[i][j]).ljust(cell_width), end='')
        print()


print_spiral_matrix(spiral_matrix(3))
print_spiral_matrix(spiral_matrix(4))
