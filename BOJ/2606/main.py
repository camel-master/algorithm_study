"""
BOJ 2606 바이러스
https://www.acmicpc.net/problem/2606

BFS를 사용하여 1번 노드 부터 연결된 모든 노드를 탐색한다.

시간복잡도
O(V + E)로 처리 가능 하므로 시간제한 1초 안으로 해결 가능하다.

공간복잡도
인접리스트로 노드 정보를 저장할 것임으로 O(V * E * 2)가 된다.
최대로 공간을 사용할 경우

정점 N개가 있을 때 간선 수는 (N-1) + (N-2) + (N-3) + ... + (N-(N-1))
N(N-1)/2개가 된다. 따라서 100개의 정점이 있는 경우
4950개의 간선을 가질 수 있으므로 약 966kb로 처리할 수 있어 공간복잡도를
통과할 수 있다.
"""
from collections import deque
import sys
f_input = sys.stdin.readline


com_cnt = int(f_input())
conn_cnt = int(f_input())

adjacency_list = [[] for _ in range(com_cnt + 1)]
for _ in range(conn_cnt):
    n1, n2 = map(int, f_input().split())
    adjacency_list[n1].append(n2)
    adjacency_list[n2].append(n1)

queue = deque()
visited = [0] * (com_cnt + 1)
queue.append(1)
visited[1] = 1
while queue:
    curr_com = queue.popleft()
    for next_com in adjacency_list[curr_com]:
        if visited[next_com] == 0:
            queue.append(next_com)
            visited[next_com] = 1

print(sum(visited) - 1)
