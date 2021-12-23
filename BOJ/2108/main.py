"""
BOJ 2108 통계학
https://www.acmicpc.net/problem/2108

산술평균: O(n)
중앙값: O(nlogn)
최빈값: O(n)
범위: 정렬되어 있는 상태라면 O(1) 아니라면 O(nlogn)

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
"""
from collections import defaultdict
import sys
f_input = sys.stdin.readline

N = int(f_input())
numbers = list()
num_dict = defaultdict(int)
total = 0
for _ in range(N):
    num = int(f_input())
    numbers.append(num)
    num_dict[num] += 1
    total += num

numbers.sort()

print(round(total/N))
print(numbers[N//2])
counts = sorted(num_dict.items(), key=lambda x: (-x[1], x[0]))
if len(counts) == 1:
    print(counts[0][0])
else:
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
print(numbers[-1] - numbers[0])
