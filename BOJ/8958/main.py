n = int(input())
ox_strings = list()
for _ in range(n):
    ox_strings.append(input())
for ox_string in ox_strings:
    count = 0
    temp = 0
    for e in ox_string:
        if e == 'O':
            temp += 1
            count += temp
        else:
            temp = 0
    print(count)
