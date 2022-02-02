"""
BOJ 13913 숨바꼭질4
https://www.acmicpc.net/problem/13913

작은 것을 완성해서 큰 덩어리를 만들어갈 수 있는 구조가 아니므로 DP문제가 아니다.

최단거리 문제이므로 BFS를 통한 탐색으로 풀어보자.

BFS 완료 후 다시 역탐색 해서 경로를 출력하니 시간제한 조건을 통과하지 못했다.
BFS 수행하면서 path를 저장해야 통과되는 모양이다.
"""
from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int, input().split())

visited = [-1] * (int(1e5) + 1)
queue = deque()
queue.append(N)
visited[N] += 1
path = dict()
l_node = 0
times = 0
while queue:
    c_node = queue.popleft()
    if c_node == K:
        times = visited[c_node]
        l_node = c_node
        break
    if c_node == 0:
        n_node = c_node + 1
        if visited[n_node] == -1:
            queue.append(n_node)
            visited[n_node] = visited[c_node] + 1
            path[n_node] = c_node
    else:
        try:
            for i in range(3):
                if i == 0:
                    n_node = c_node - 1
                elif i == 1:
                    n_node = c_node + 1
                else:
                    n_node = c_node * 2
                if visited[n_node] == -1:
                    queue.append(n_node)
                    visited[n_node] = visited[c_node] + 1
                    path[n_node] = c_node

        except IndexError:
            pass

print(times)

if not path.items():
    print(c_node)
else:
    res = [c_node]
    while True:
        res.append(path[c_node])
        if path[c_node] == N:
            break
        c_node = path[c_node]
    print(*res[-1::-1])

# path = [pos]
# while True:
#     c_times = visited[path[-1]]
#     if path[-1] % 2 == 0:
#         if visited[path[-1] // 2] == c_times - 1:
#             path.append(path[-1] // 2)
#             continue
#
#     if visited[path[-1] - 1] == c_times - 1:
#         path.append(path[-1] - 1)
#         continue
#     elif visited[path[-1] + 1] == c_times - 1:
#         path.append(path[-1] + 1)
#
#     if path[-1] == N:
#         break