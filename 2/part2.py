def in_range(n1, n2, n3):
    diff1 = abs(n1 - n2)
    diff2 = abs(n2 - n3)
    return  diff1 > 0 and diff1 < 4 and diff2 > 0 and diff2 < 4

# def func():
#     counter = 0
#     with open("input_test.txt") as f:
#         data = f.read().splitlines()
#         for line in data:
#             if data.index(line) == 0:
#                 continue

#             if data.index(line) > 1:
#                 break

#             print("Line", line)

#             values = [int(i) for i in line.split(" ")]

#             ok = True
#             safe = True

#             decreasing = None

#             for value_id in range(0, len(values)-1):
#                 print("Decreasing", decreasing, values[value_id], values[value_id+1])

#                 if values[value_id] == values[value_id+1]:
#                     if safe:
#                         print("Safe", values[value_id], values[value_id+1])
#                         safe = False
#                         continue

#                 # This is an increasing sequence
#                 elif values[value_id] < values[value_id+1]:
#                     if decreasing is not None and decreasing == True:
#                         print("Not decreasing anymore", values[value_id], values[value_id+1])
#                         if safe:
#                             print("Safe", values[value_id], values[value_id+1])
#                             safe = False
#                             continue
#                     else:
#                         print("Still decreasing", values[value_id], values[value_id+1])
#                         decreasing = False

#                 # This is a decreasing sequence
#                 elif values[value_id] > values[value_id+1]:
#                     if decreasing is not None and decreasing == False:
#                         print("Not increasing anymore", values[value_id], values[value_id+1])
#                         if safe:
#                             print("Safe", values[value_id], values[value_id+1])
#                             safe = False
#                         continue
#                     else:
#                         print("Still increasing", values[value_id], values[value_id+1])
#                         decreasing = True

#             if ok:
#                 counter += 1

#     print(counter)


def safe (values, msg):
    for value_id in range(1, len(values)-1):
        if  not (values[value_id-1] < values[value_id] and values[value_id] < values[value_id+1]) and \
            not (values[value_id-1] > values[value_id] and values[value_id] > values[value_id+1]):
            # print("Values not in increasing or decreasing order", values[value_id-1], values[value_id], values[value_id+1])
            msg += "Values not in increasing or decreasing order {} {} {}\n".format(values[value_id-1], values[value_id], values[value_id+1])
            return False, value_id, msg
        if not in_range(values[value_id-1], values[value_id], values[value_id+1]):
            # print("Values not in range
            msg += "Values not in range {} {} {}\n".format(values[value_id-1], values[value_id], values[value_id+1])
            return False, value_id, msg
    return True, None, msg

def func():
    counter = 0
    with open("input1.txt") as f:
        data = f.read().splitlines()

        for line in data:
            values = [int(i) for i in line.split(" ")]

            msg = ""

            s, id, msg= safe(values, msg)

            if s:
                counter += 1
            else:
                # new_values = deepcopy(values)
                new_values = values[:id-1] + values[id:]
                s, _, msg= safe(new_values, msg)

                if s:
                    counter += 1
                else:
                    new_values = values[:id] + values[id+1:]
                    # new_values = values.copy().remove(values[id])
                    s, _, msg= safe(new_values, msg)

                    if s:
                        counter += 1
                    elif id == len(values) - 2:
                        s, _, msg= safe(values[:id], msg)
                        if s:
                            counter += 1
                        else:
                            print("Skipping line", line, "\n", msg)
                            continue
                    else:
                        print("Skipping line", line, "\n", msg)
                        continue


        print("Counter", counter)
        print()

                



if __name__ == "__main__":
    func()