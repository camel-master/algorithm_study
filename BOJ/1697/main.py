"""
BOJ 1697 숨바꼭질
https://www.acmicpc.net/problem/1697

0 <= N, K <= 100,000


"""
from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int, input().split())

visited = [-1] * (int(1e5) + 1)
queue = deque()
queue.append(N)
visited[N] += 1
while queue:
    c_node = queue.popleft()
    if c_node == K:
        print(visited[c_node])
        break
    if c_node == 0:
        if visited[c_node + 1] == -1:
            queue.append(c_node + 1)
            visited[c_node + 1] = visited[c_node] + 1
    else:
        try:
            if visited[c_node - 1] == -1:
                queue.append(c_node - 1)
                visited[c_node - 1] = visited[c_node] + 1
            if visited[c_node + 1] == -1:
                queue.append(c_node + 1)
                visited[c_node + 1] = visited[c_node] + 1
            if visited[c_node * 2] == -1:
                queue.append(c_node * 2)
                visited[c_node * 2] = visited[c_node] + 1
        except IndexError:
            pass
