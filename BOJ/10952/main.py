import sys
input_list = list()
while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0:
        break
    input_list.append(a + b)
for e in input_list:
    print(e)
