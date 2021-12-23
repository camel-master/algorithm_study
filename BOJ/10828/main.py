"""
BOJ 10828 스택
https://www.acmicpc.net/problem/10828

리스트 타입이 stack과 동일하게 동작하므로 리스트 타입을 사용하여 구현한다.

push, pop, size, empty, top 모두 O(1) 복잡도이고, 모든 명령을 각각
수행하므로 O(N)의 시간복잡도로 처리 가능하다.
N <= 10000 이므로 제한 시간 0.5초 이내로 수행 가능하다.
메모리의 N개의 연산을 모두 push에 사용할 경우 최대 10,000개의 정수형 자료를 저장할 메모리가 필요하므로
이 로직을 수행하는데 필요한 최대 메모리는 약 0.4MB이기 때문에 메모리 제한을 통과할 수 있다.
"""
import sys
f_input = sys.stdin.readline
stack = list()
N = int(f_input())
for _ in range(N):
    instruction = list(map(str, f_input().rstrip().split()))
    if len(instruction) > 1:
        cmd = instruction[0]
        arg = instruction[1]
    else:
        cmd = instruction[0]
    if cmd == 'push':
        stack.append(arg)
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
