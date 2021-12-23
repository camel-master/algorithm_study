"""
BOJ 11650 좌표 정렬하기
https://www.acmicpc.net/problem/11650

좌표를 x축 오름 차순으로 정렬 후
x축의 순서가 흩어지지 않는 상태에서 y축 오름 차순으로 정렬 한다.
"""
import sys
f_input = sys.stdin.readline

N = int(f_input())
coordinates = list()
for _ in range(N):
    coordinates.append(tuple(map(int, f_input().split())))
coordinates.sort(key=lambda x:(x[0], x[1]))
for x, y in coordinates:
    print(x, y)
