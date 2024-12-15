def correct_input(pages, rule, rules):
    index1 = pages.index(rule[0])
    index2 = pages.index(rule[1])
    pages[index1], pages[index2] = pages[index2], pages[index1]

    for rule in rules:
        if rule[0] in pages and rule[1] in pages and pages.index(rule[0]) > pages.index(rule[1]):
            pages = correct_input(pages, rule, rules)

    return pages

def check_input(pages, rules):
    correct = True
    for rule in rules:
        if rule[0] in pages and rule[1] in pages and pages.index(rule[0]) > pages.index(rule[1]):
            correct = False
            pages = correct_input(pages, rule, rules)
        

    if not correct:
        if len(pages)%2 == 0:
            raise Exception('Even number of pages')
        else:
            return pages[len(pages)//2]
    else:
        return 0
    

def func():
    sum = 0
    with open('input.txt') as f:
        inputs = False
        rules = []
        for line in f:
            if len(line.strip()) == 0:
                inputs = True
                continue

            if inputs:
                pages = [int(x) for x in line.split(',')]
                print(pages)
                sum += check_input(pages, rules)

            else:
                rules.append((int(line.split('|')[0]), int(line.split('|')[1])))
                print(line, rules[-1])

    print(sum)




if __name__ == '__main__':
    func()