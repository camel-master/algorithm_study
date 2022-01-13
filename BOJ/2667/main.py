"""
BOJ 2667 단지번호붙이기
https://www.acmicpc.net/problem/2667

지도를 한 칸씩 탐색하다가 집을 만나면 BFS를 돈다.
붙어있는 모든 집에 대해 탐색을 완료 하면  방문한 적이 없는 다른 집을
탐색한다. 발견되면 다시 BFS를 실행한다.
이렇게 하면서 단지별로 집을 카운팅한 결과를 리스트에 넣는다.
리스트를 오름차순 정렬하여 출력한다.

전체 맵을 탐색하는데 O(N^2)
집이 발견되면 BFS를 도는데 O(V + E)의 시간복잡도이다.

"""
from collections import deque
import sys
f_input = sys.stdin.readline


N = int(f_input())
map_info = [f_input().rstrip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]

queue = deque()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

house_cnts = list()

for r in range(N):
    for c in range(N):
        if map_info[r][c] == '1' and visited[r][c] == 0:
            h_cnt = 0
            queue.append((r, c))
            visited[r][c] = 1
            h_cnt += 1
            # 카운팅 로직 추가
            while queue:
                cr, cc = queue.popleft()
                for d in range(4):
                    nr = cr + dy[d]
                    nc = cc + dx[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if map_info[nr][nc] == '1' and visited[nr][nc] == 0:
                            queue.append((nr, nc))
                            visited[nr][nc] = 1
                            h_cnt += 1
            house_cnts.append(h_cnt)

house_cnts.sort()
print(len(house_cnts))
for cnt in house_cnts:
    print(cnt)