import re

MUL_RE = r'mul\((?P<x>\d+),(?P<y>\d+)\)'

def comp(line):
    counter = 0 
    for match in re.finditer(MUL_RE, line):
        x = int(match.group('x'))
        y = int(match.group('y'))
        counter += x * y

    return counter


def func():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        mul_count = 0
        for line in lines:
            instructions = []
            tmp_instructions = line.split("don't()")
            print(tmp_instructions)
            instructions.append(tmp_instructions[0])
            for instruction in tmp_instructions:
                if "do()" in instruction:
                    instructions.append(instruction.split("do()")[1])

            for instruction in instructions:
                print(instruction)
                mul_count += comp(instruction)
                
        print(mul_count)

if __name__ == '__main__':
    func()