"""
BOJ 1629 곱셈
https://www.acmicpc.net/problem/1629

단순히 A ** B % C로 계산해보고자 했으나, ** 연산이 선형으로 곱해가기 때문에
B = 2^31 - 1 인 경우 2147483647 만큼의 곱연산을 하게 된다. 따라서 다음과 같이
while B > 0
    B % 2 * A**1
    B = B // 2

10 10 10 10 10 10 10 10 10 10 10    (11개)
100 100 100 100 100     10          (5개)
10000 10000         100 10          (2개)
100000000           100 10          (1개)

POW()를 사용한 간단한 풀이.
print(pow(*map(int,input().split())))

"""
import sys

f_input = sys.stdin.readline

A, B, C = map(int, f_input().split())

res = 1
power = 1
while B > 0:
    if res == 0:
        break
    if B % 2 != 0:
        res *= A
    res %= C
    B //= 2
    power *= 2
    A *= A % C

print(res)
