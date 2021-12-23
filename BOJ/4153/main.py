"""
BOJ 4153 직각삼각형
https://www.acmicpc.net/problem/4153

3:4:5 비율의 삼각형이 직각삼각형이다.
주어지는 입력들의 비율이 3:4:5를 만족하는지 확인하여
만족하는 경우 "right"를 만족하지 않는 경우 "wrong"을 출력한다.


입력 값이 0 0 0 인 경우 종료한다.


base = [3, 4, 5]
입력 값을 오름차순 정렬한다.

data[0] == base[0]이 될 때까지 각 선분을 base로 나눈 값으로 대체한다.
나눠 떨어지지 않는 경우가 있다면 비율이 맞지않는 경우이다.

위와 같이 생각했으나 입력으로 주어진 5, 12, 13은 3:4:5를 만족하지 않는 다른 비율의 직각삼각형이다.
따라서 이 문제는 가장 긴변의 제곱 = 나머지 변 중 하나의 제곱 + 또다른 남은 변 중 하나의 제곱 을 만족하는
삼각형을 구하는 문제가 되겠다.
"""
# import sys
# f_input = sys.stdin.readline
# base = [3, 4, 5]
# while True:
#     triangle = list(map(int, f_input().split()))
#     if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
#         break
#     triangle.sort()
#     while triangle[0] > base[0]:
#         for i in range(3):
#             print(triangle[i], base[i])
#             triangle[i] //= base[i]
#         print(triangle)
#     if triangle[0] == 3 and triangle[1] == 4 and triangle[2] == 5:
#         print('right')
#     else:
#         print('wrong')
# 세 수의 GCD를 구하기.
# 가장 작은 수를 확인한다.
# 2 ~ 가장 작은 수 까지로 세 수를 나눴을 때 모든 수가 나눠 떨어지는 가장 큰 수가 최대 공약 수가 된다.
import sys
f_input = sys.stdin.readline
while True:
    triangles = list(map(int, f_input().split()))
    if triangles[0] == triangles[1] == triangles[2] == 0:
        break
    triangles.sort()
    if triangles[2] ** 2 == triangles[0] ** 2 + triangles[1] ** 2:
        print('right')
    else:
        print('wrong')
