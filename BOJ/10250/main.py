"""
BOJ 10250 ACM 호텔
https://www.acmicpc.net/problem/10250

아래층의 가장 빠른 호수 부터 배정에 사용해야 한다.
H x W = 3 x 3인 경우
101, 201, 301, 102, 202, 302, 103, 203, 303 순으로 방이 배정되어야 하겠다.

각 호수 별로 모든 층에 대해 확인해야 하므로 O(n^2) 으로 처리할 수 있다.
좀더 속도를 개선하기 위해 하나씩 모두 탐색하기 보다 다음과 같이 계산해보자.
room_number = 1 + N // H
floor_number = N % H
반복문을 수행하지 않고도 N번째 방을 구할 수 있으므로 O(1)에 해결이 가능하다.

1
4 7 4
expected: 401
"""
import sys
f_input = sys.stdin.readline

T = int(f_input())
for _ in range(T):
    H, W, N = map(int, f_input().rstrip().split())

    if N % H == 0:
        floor_number = str(H)
        room_number = N // H
    else:
        floor_number = str(N % H)
        room_number = N // H + 1
    if room_number < 10:
        room_number = '0' + str(room_number)
    else:
        room_number = str(room_number)
    print(floor_number + room_number)
