"""
BOJ 2965 캥거루 세 마리
https://www.acmicpc.net/problem/2965

입력값 2 3 5 를 살펴보자.
_##_#____
123456789

__###____
123456789


입력값 3 5 9
__#_#___#
123456789
____#__##
123456789
____##_#_
123456789
_____###_
123456789

가장 왼쪽의 캥거루 위치를 A, 중간 캥거루 위치를 B, 오른쪽 캥거루 위치를 C 이라 하자.
if (B - A) <= (C - B) then L이 C-1로 점프한다.
    A = B
    B = C - 1
else R이 L + 1로 점프한다.
    C = B
    B = A + 1


점프하는 위치에 다른 캥거루가 없으면 카운터를 증가시킨다.

절반씩 범위를 줄여가면서 이동 가능 여부를 확인하게 되므로 O(log N)에 처리 가능하다.

"""
A, B, C = map(int, input().split())
count = 0
while True:
    if B - A < 2 and C - B < 2:
        print(count)
        break
    else:
        count += 1

    if (B - A) <= (C - B):
        A = B
        B = C - 1
    else:
        C = B
        B = A + 1
