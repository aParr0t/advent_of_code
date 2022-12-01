# read input
with open('input.txt') as f:
    scanners = []
    lines = [s.rstrip() for s in f.readlines() if s != '\n']
    for s in lines:
        if 'scanner' in s:
            scanners.append([])
        else:
            pos = [int(x) for x in s.split(',')]
            scanners[-1].append(pos)
    # print('scanners:')
    # for scanner in scanners:
    #     print(scanner)

#----------part 1

#----------part 1

#----------part 2

#----------part 2