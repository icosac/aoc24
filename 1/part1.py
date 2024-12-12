#!/usr/bin/env python3

import re

re_str= r"(\d+)\s+(\d+)"

def func():
    L1 = []
    L2 = []
    with open("input1.txt") as f:
        for line in f:
            x, y = re.match(re_str, line).groups()

            L1.append(int(x))
            L2.append(int(y))

    L1.sort()
    L2.sort()

    print(sum([abs(a-b) for a, b in zip(L1, L2)]))
    

if __name__ == "__main__":
    func()