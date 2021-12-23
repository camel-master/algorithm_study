import sys
n = sys.stdin.readline().rstrip()
if int(n) < 10:
    n = '0' + n
temp = n
cycle = 0
while True:
    result = int(temp[0]) + int(temp[1])
    temp = temp[1] + str(result % 10)
    cycle += 1
    if temp == n:
        break
print(cycle)
