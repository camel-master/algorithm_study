"""
BOJ 9012 괄호
https://www.acmicpc.net/problem/9012

stack을 사용하여 푸는 문제다.
선형탐색 하면서 괄호 방향에 맞춰 stack에 넣고 빼며 마지막에 stack이 비어있으면
yes를 출력 아니라면 no를 출력하도록 작성한다.
n의 길이는 최대 50이므로 O(n) 시간복잡도로 해결 가능.

"""
import sys
f_input = sys.stdin.readline


def confirm_vps(string):
    stack = list()
    for ch in string:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


T = int(f_input())
for _ in range(T):
    if confirm_vps(f_input().rstrip()):
        print('YES')
    else:
        print('NO')
