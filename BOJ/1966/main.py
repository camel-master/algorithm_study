"""
BOJ 1966 프린터 큐
https://www.acmicpc.net/problem/1966


"""
from collections import deque

T = int(input())
test = list()
for i in range(T):
    N, M = map(int, input().split())
    queue = deque((e[0], e[1]) for e in enumerate(list(map(int, input().split()))))
    answer = 0
    while queue:
        p_data = queue.popleft()
        if any(p_data[1] < q_data[1] for q_data in queue):
            queue.append(p_data)
        else:
            answer += 1
            if p_data[0] == M:
                print(answer)
