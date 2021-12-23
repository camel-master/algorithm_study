"""
BOJ 10845 큐
https://www.acmicpc.net/problem/10845


"""
from collections import deque
import sys
f_input = sys.stdin.readline

queue = deque()
N = int(f_input())
for _ in range(N):
    ins = f_input().rstrip().split()
    cmd = ''
    arg = ''
    if len(ins) > 1:
        cmd, arg = ins
    else:
        cmd = ins[0]
    if cmd == 'push':
        queue.append(arg)
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
