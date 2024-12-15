def func():
    matrix = []
    with open('input.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    if len(matrix[-1]) == 0:
        matrix = matrix[:-1]

    print(matrix)

    counter = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if matrix[i][j] == 'A':
                if ((matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or 
                    (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or
                    (matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M') or
                    (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M')):
                    counter += 1 
                    print('Cross at', i, j) 
            
    print(counter)

if __name__ == '__main__':
    func()