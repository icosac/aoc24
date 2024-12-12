def in_range(n1, n2, n3):
    diff1 = abs(n1 - n2)
    diff2 = abs(n2 - n3)
    return  diff1 > 0 and diff1 < 4 and diff2 > 0 and diff2 < 4

def safe (values):
    for value_id in range(1, len(values)-1):
        if  not (values[value_id-1] < values[value_id] and values[value_id] < values[value_id+1]) and \
            not (values[value_id-1] > values[value_id] and values[value_id] > values[value_id+1]):
            print("Values not in increasing or decreasing order", values[value_id-1], values[value_id], values[value_id+1])
            return False
        if not in_range(values[value_id-1], values[value_id], values[value_id+1]):
            print("Values not in range", values[value_id-1], values[value_id], values[value_id+1])
            return False
    return True

def func():
    counter = 0
    with open("input1.txt") as f:
        for line in f:
            values = [int(i) for i in line.split(" ")]
            
            if safe(values):
                counter += 1

    print(counter)


                



if __name__ == "__main__":
    func()