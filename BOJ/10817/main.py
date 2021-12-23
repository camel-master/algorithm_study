import sys
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort(reverse=True)
print(numbers[1])
