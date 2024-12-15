def print_matrix(matrix):
    # return
    for row in matrix:
        print(''.join(row))
    # with open('output.txt', 'w') as f:
        # for row in matrix:
            # f.write(''.join(row) + '\n')

def move_until_obstacle(matrix, pos, direction):
    # print("Guard is in", pos, "moving", direction)
    if direction == 0: # up
        while matrix[pos[0]][pos[1]] != '#':
            matrix[pos[0]][pos[1]] = 'X'
            pos[0] -= 1
            if pos[0] < 0:
                return True
        pos[0] += 1
    elif direction == 1: # right
        while matrix[pos[0]][pos[1]] != '#':
            matrix[pos[0]][pos[1]] = 'X'
            pos[1] += 1
            if pos[1] >= len(matrix[pos[0]]):
                return True
        pos[1] -= 1
    elif direction == 2: # down
        while matrix[pos[0]][pos[1]] != '#':
            matrix[pos[0]][pos[1]] = 'X'
            pos[0] += 1
            if pos[0] >= len(matrix):
                return True
        pos[0] -= 1
    elif direction == 3: # left
        while matrix[pos[0]][pos[1]] != '#':
            matrix[pos[0]][pos[1]] = 'X'
            pos[1] -= 1
            if pos[1] < 0:
                return True
        pos[1] += 1
    
    return False


def func():
    matrix = []
    init_pos = []
    with open('input.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))

            if len(init_pos) == 0:
                for i in range(len(line)):
                    if line[i] == '^':
                        init_pos = [len(matrix)-1, i]
            
    if len(matrix[-1]) == 0:
        matrix.pop()
    print_matrix(matrix)

    exited = False
    direction = 0

    while not exited:
        exited = move_until_obstacle(matrix, init_pos, direction)
        direction = (direction + 1) % 4
        print("Guard moved to", init_pos)

    counter = 0
    for row in matrix:
        for cell in row:
            if cell == 'X':
                counter += 1

    print("Guard moved of", counter, "steps")


if __name__ == '__main__':
    func()