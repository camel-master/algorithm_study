"""
BOJ 11050 이항 계수 1
https://www.acmicpc.net/problem/11050

이항계수... 조합 수를 구하면 된다.
"""
import math
import sys
f_input = sys.stdin.readline

N, K = map(int, f_input().split())
#nCr = nPr / r! = n * (n - 1) * (n - 2) * ... * (n - r + 1) / r!
H = 1
n = N
while n >= N - K + 1:
    H *= n
    n -= 1
print(H // math.factorial(K))
