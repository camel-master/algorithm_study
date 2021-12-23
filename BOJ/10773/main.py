"""
BOJ 10773 제로
https://www.acmicpc.net/problem/10773

stack을 사용하여 해결.
O(K)로 처리가능. 1 <= K <= 100,000 이므로 제한시간 1초 내로 풀이 가능.
"""
import sys
f_input = sys.stdin.readline


K = int(f_input())
stack = list()
for _ in range(K):
    data = int(f_input())
    if data != 0:
        stack.append(data)
    else:
        stack.pop()

print(sum(stack))
