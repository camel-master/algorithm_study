"""
BOJ 10866 덱
https://www.acmicpc.net/problem/10866


"""
from collections import deque
import sys
f_input  = sys.stdin.readline

N = int(f_input())
dq = deque()
for _ in range(N):
    ins = f_input().split()
    cmd = ins[0]
    arg = ''
    if len(ins) > 1:
        arg = ins[1]

    if cmd == 'push_front':
        dq.appendleft(arg)
    elif cmd == 'push_back':
        dq.append(arg)
    elif cmd == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
