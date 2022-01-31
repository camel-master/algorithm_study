"""
BOJ 2156 포도주 시식
https://www.acmicpc.net/problem/2156


f(n) = n번의 위치에서 마실 수 있는 포도주의 최대량
f(n) = max(
            f(n-3) + (n-1) + n,
            f(n-2) + n,
            f(n-1)
        )

"""
import sys

f_input = sys.stdin.readline


def get_max_amt():
    N = int(f_input())
    wine_amt = []
    for i in range(N):
        wine_amt.append(int(f_input()))

    dp = [0] * (N + 1)
    dp[1] = wine_amt[0]
    if N == 1:
        return dp[1]

    dp[2] = wine_amt[0] + wine_amt[1]
    if N == 2:
        return dp[2]

    for i in range(3, N + 1):
        a = dp[i-3] + wine_amt[i-2] + wine_amt[i-1]
        b = dp[i-2] + wine_amt[i-1]
        c = dp[i-1]
        dp[i] = max(a, b, c)

    return dp[-1]


print(get_max_amt())


# import sys
#
# f_input = sys.stdin.readline
#
# N = int(f_input())
# wine_amt = []
# for _ in range(N):
#     wine_amt.append(int(f_input()))
#
# dp = [0] * N
# dp[0] = wine_amt[0]
# dp[1] = wine_amt[0] + wine_amt[1]
# dp[2] = max(wine_amt[0], wine_amt[1]) + wine_amt[2]
#
# for i in range(3, N):
#     a = dp[i-3] + wine_amt[i-1] + wine_amt[i]
#     b = dp[i-2] + wine_amt[i]
#     c = dp[i-1]
#     dp[i] = max(a, b, c)
#
# print(dp[-1])
# import sys
#
# N = int(sys.stdin.readline())
# wine_amt = [0]
# for _ in range(N):
#     wine_amt.append(int(sys.stdin.readline()))
#
# dp = [0]
# dp.append(wine_amt[1])
# dp.append(wine_amt[1] + wine_amt[2])
# dp.append(max(wine_amt[1], wine_amt[2]) + wine_amt[3])
#
# for i in range(4, N + 1):
#     # dp.append(dp[i-3] + max(wine_amt[i-2], wine_amt[i-1]) + wine_amt[i])
#     dp.append(max(dp[i-2], dp[i-3] + wine_amt[i-1]) + wine_amt[i])
#
# print(dp)

# import sys
#
# N = int(sys.stdin.readline())
# wine_amt = [0]
# for _ in range(N):
#     wine_amt.append(int(sys.stdin.readline()))
#
# d1 = [0] * (N + 1)
# d2 = [0] * (N + 1)
# max_amt = 0
# for i in range(1, N + 1):
#     d1[i] = d2[i-1] + wine_amt[i]
#     d2[i] = max(d1[i-2], d2[i-2]) + wine_amt[i]
#     if max(d1[i], d2[i]) > max_amt:
#         max_amt = max(d1[i], d2[i])
# print(d1)
# print(d2)
# print(max_amt)
