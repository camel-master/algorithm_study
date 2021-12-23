import sys
n = int(sys.stdin.readline().rstrip())
output_list = list()
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    output_list.append(a + b)
for e in output_list:
    print(e)
