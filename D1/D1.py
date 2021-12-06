with open('/Users/whaley/Dev/AOC21/D1/d1_input.txt') as f:
    a = [f.readlines(), 0]
    while len(a[0]) - 1: a[1] += (int(a[0].pop(0)) < int(a[0][0]))
    print(a[1])
