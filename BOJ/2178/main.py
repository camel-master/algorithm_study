"""
BOJ 2178 미로탐색
https://www.acmicpc.net/problem/2178

전형적인 BFS 문제로 본다.
BFS를 수행하면서 노드를 방문할 때 이동거리 + 1을 해주면 얼마나 이동했는지
알 수 있다. 이 때 현재 위치에서 방문할 수 있는 노드가 없는 경우
현재 위치가 (N, M)이면 이동거리를 출력하고
현재 위치가 (N, M)이 아니라면 이동거리를 -1해준다.

시간복잡도
BFS의 시간복잡도는 O(V + E)이고 N, M의 최댓값은 각각 100이므로 100 + 100 = 200회의 연산이 필요하다.
따라 제한시간인 1초 안에 해를 구할 수 있다.

공간복잡도
N * M * 4 Byte = 40000 byte = 39kb로 BFS를 수행하기에 부족함이 없다.
"""
from collections import deque
import sys
f_input = sys.stdin.readline


N, M = map(int, f_input().split())
map_info = ['0' * (M + 1)]
for _ in range(N):
    map_info.append('0' + f_input().rstrip())

queue = deque()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[0] * (M + 1) for _ in range(N + 1)]
visited[1][1] = 1
queue.append((1, 1))
while queue:
    cr, cc = queue.popleft()
    if cr == N and cc == M:
        print(visited[cr][cc])
        break
    for d in range(4):
        nr = cr + dy[d]
        nc = cc + dx[d]
        if 1 <= nr <= N and 1 <= nc <= M:
            if map_info[nr][nc] == '1' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[cr][cc] + 1
                queue.append((nr, nc))
