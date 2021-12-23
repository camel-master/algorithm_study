candy = int(input())

count = 0
for T in range(candy + 1):
    if T % 2 != 0:
        continue
    for Y in range(candy + 1 - T):
        for N in range(candy + 1 - T - Y):
            if N < Y + 2:
                continue
            if T + Y + N == candy and T != 0 and Y != 0 and N != 0:
                # print(f'Taek-hee:{T}, Young-hoon:{Y}, Nam-gyu:{N}')
                count += 1

print(count)
