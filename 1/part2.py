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

    occur = { x: 0 for x in L1 }

    for i in L1:
        if occur[i] > 0:
            continue
        for j in L2:
            if i == j:
                occur[i] += 1
    
    print(sum([occur[i] * i for i in L1]))

if __name__ == "__main__":
    func()