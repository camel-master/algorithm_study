N = int(input())

INF = 1000001
dp_table = [INF] * (N + 1)
dp_table[0] = 0
dp_table[1] = 0
for i in range(2, N + 1):
    if i % 2 == 0 and i % 3 != 0:
        dp_table[i] = min(dp_table[i // 2], dp_table[i - 1]) + 1
    elif i % 2 != 0 and i % 3 == 0:
        dp_table[i] = min(dp_table[i // 3], dp_table[i - 1]) + 1
    elif i % 2 == 0 and i % 3 == 0:
        dp_table[i] = min(dp_table[i//2], dp_table[i // 3], dp_table[i - 1]) + 1
    else:
        dp_table[i] = dp_table[i - 1] + 1

print(dp_table[N])