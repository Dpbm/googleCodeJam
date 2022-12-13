T = int(input())

inputs = []

for _ in range(T):
    inputs.append(list(map(int, input().split())))


for case in range(T):
    print(f'Case #{case+1}:')

    R, C = inputs[case]

    totalRows = R * 2 + 1

    for i in range(totalRows):
        firstPoints = 1 if i < 2 else 0

        line = '..' * firstPoints

        if(i % 2 == 0):
            line += ('+-' * (C - (len(line)//2))) + '+'
        else:
            line += ('|.' * (C - (len(line)//2))) + '|'

        print(line)

