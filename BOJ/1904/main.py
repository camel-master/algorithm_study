"""
BOJ 1904 01타일
https://www.acmicpc.net/problem/1904

N = 1
    1
N = 2
    11
    00
N = 3
    001
    100
    111
N = 4
    0000
    0011
    1001
    1100
    1111
N = 5
    00001
    00100
    10000
    00111
    10011
    11001
    11100
    11111
N = 6
    000000
    000011
    001001
    100001
    100100
    110000
    001111
    100111
    110011
    111001
    111100
    111111
N = 7
    0000001
    0000100
    0010000
    1000000
    0000111
    0010011
    1000011
    1001001
    1100001
    1100100
    1110000
    0011111
    1001111
    1100111
    1110011
    1111001
    1111100
    1111111


N - 2 항의 요소들에 00을 앞뒤로 붙인 요소 +
N - 1 항의 요소들에 1을 앞뒤로 붙인 요소
중 중복을 제외한 요소들의 수.

f(1) = 1, f(2) = 2
f(3) = f(1) + f(2)
f(N) = f(N-2) + f(N-1)
"""
import sys

f_input = sys.stdin.readline

N = int(f_input())
dp = [1, 2, 0]
if N < 3:
    print(dp[N-1])
else:
    for _ in range(3, N + 1):
        dp[2] = (dp[0] + dp[1]) % 15746
        dp[0] = dp[1]
        dp[1] = dp[2]

    print(dp[2])
