"""
BOJ 18513 샘터
https://www.acmicpc.net/problem/18513

샘터 들을 기준 점으로 잡고 바로 옆의 위치부터 집을 이어서 지어나간다.
[공 공 샘 공 공 샘 공] 과같이 있다고 하면 다음 단계는
[공 집 샘 집 집 샘 집] 이고 다음 단계는
[집 집 샘 집 집 샘 집] 이 된다.
즉 level 별로 접근해서 샘과의 거리를 계산해야 한다.
따라서 BFS를 사용하여 풀어보도록 한다.
샘터의 위치가 -100,000,000 ~ 100,000,000 이므로
총 200,000,000의 node가 존재하고 수직선 상에 모두 연결되어 있으므로 199,999,999 개의
간선이 존재한다. BFS 시간복잡도는 O(E + V)이므로 최대 약 4억번의 연산을 수행하게 된다.
제한 시간 안에 수행될 수 있을 것으로 예상된다.
"""
from collections import deque
import sys

f_input = sys.stdin.readline

N, K = map(int, f_input().split())
queue = deque()
visited = dict()
for spring_pos in map(int, f_input().split()):
    queue.append(spring_pos)
    visited[spring_pos] = 0
min_pos = min(queue) - K
max_pos = max(queue) + K

house_cnt = 0
unhappy_pnt = 0
while queue:
    c_pos = queue.popleft()
    if min_pos <= c_pos - 1:
        if not visited.__contains__(c_pos - 1):
            queue.append(c_pos - 1)
            visited[c_pos - 1] = visited[c_pos] + 1
            unhappy_pnt += visited[c_pos - 1]
            house_cnt += 1
            if house_cnt == K:
                break
    if c_pos + 1 <= max_pos:
        if not visited.__contains__(c_pos + 1):
            queue.append(c_pos + 1)
            visited[c_pos+1] = visited[c_pos] + 1
            unhappy_pnt += visited[c_pos+1]
            house_cnt += 1
            if house_cnt == K:
                break
print(unhappy_pnt)
