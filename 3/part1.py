import re

MUL_RE = r'mul\((?P<x>\d+),(?P<y>\d+)\)'

def func():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        mul_count = 0
        for line in lines:
            for match in re.finditer(MUL_RE, line):
                x = int(match.group('x'))
                y = int(match.group('y'))
                print(f'{x} * {y} = {x * y}')
                mul_count += x * y

        print(mul_count)

if __name__ == '__main__':
    func()