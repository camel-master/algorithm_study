import sys
h, m = map(int, sys.stdin.readline().rstrip().split())
if m - 45 < 0:
    h -= 1
    if h < 0:
        h = 23
    m = 15 + m # 60 + m - 45
else:
    m -= 45
print(h, m)
