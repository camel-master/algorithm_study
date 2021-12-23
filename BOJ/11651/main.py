"""
BOJ 11651 좌표 정렬하기 2
https://www.acmicpc.net/problem/11651

좌표 정렬하기 1 문제에서 primary: x, secondary: y 였던 정렬 순서를 반대로 바꿔서
primary: y, secondary: x로 하여 정렬한 결과를 반환한다.
"""
import sys
f_input = sys.stdin.readline

N = int(f_input())
coordinates = list()
for _ in range(N):
    coordinates.append(tuple(map(int, f_input().split())))
coordinates.sort(key=lambda x: (x[1], x[0]))
for x, y in coordinates:
    print(x, y)
