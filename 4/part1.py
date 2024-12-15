def func():
    matrix = []
    with open('input.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    if len(matrix[-1]) == 0:
        matrix = matrix[:-1]

    print(matrix)

    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Horizontal forward
            if matrix[i][j] == 'X' and j < len(matrix[i]) - 3:
                try:
                    if matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
                        print('Horizontal forward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Horizontal forward IndexError at", i, j)
            # Horizontal backward
            if matrix[i][j] == 'S' and j < len(matrix[i]) - 3:
                try:
                    if matrix[i][j+1] == 'A' and matrix[i][j+2] == 'M' and matrix[i][j+3] == 'X':
                        print('Horizontal backward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Horizontal backward IndexError at", i, j)

            # Vertical forward
            if matrix[i][j] == 'X' and i < len(matrix) - 3:
                try:
                    if matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
                        print('Vertical forward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Vertical forward IndexError at", i, j)
            # Vertical backward
            if matrix[i][j] == 'S' and i < len(matrix) - 3:
                try:
                    if matrix[i+1][j] == 'A' and matrix[i+2][j] == 'M' and matrix[i+3][j] == 'X':
                        print('Vertical backward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Vertical backward IndexError at", i, j)

            # Diagonal forward down
            if matrix[i][j] == 'X' and i < len(matrix) - 3 and j < len(matrix[i]) - 3:
                try:
                    if matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
                        print('Diagonal forward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Diagonal forward IndexError at", i, j)
            # Diagonal forward up
            if matrix[i][j] == 'X' and i > 2 and j < len(matrix[i]) - 3:
                try:
                    if matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
                        print('Diagonal forward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Diagonal forward IndexError at", i, j)
            # Diagonal backward down
            if matrix[i][j] == 'S' and i < len(matrix) - 3 and j < len(matrix[i]) - 3:
                try:
                    if matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'M' and matrix[i+3][j+3] == 'X':
                        print('Diagonal backward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Diagonal backward IndexError at", i, j)
            # Diagonal backward up
            if matrix[i][j] == 'S' and i > 2 and j < len(matrix[i]) - 3:
                try:
                    if matrix[i-1][j+1] == 'A' and matrix[i-2][j+2] == 'M' and matrix[i-3][j+3] == 'X':
                        print('Diagonal backward at', i, j)
                        counter += 1
                except IndexError as e:
                    print("Diagonal backward IndexError at", i, j)
            
    print(counter)

if __name__ == '__main__':
    func()