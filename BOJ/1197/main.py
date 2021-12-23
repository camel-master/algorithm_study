"""
BOJ 1197 최소 스패닝 트리
https://www.acmicpc.net/problem/1197

최소 스패닝 트리를 찾는 문제다.
간선을 가중치 오름차순으로 하여 정렬한다.

가장 낮은 가중치의 간선을 선택 했을 때 순환이 발생하지 않는다면 간선으로 연결된 두 정점을 연결처리한다.
순환이 발생한다면 해당 간선은 무시하고 다음 가중치의 간선을 선택하여 위의 작업을 진행한다.
정점 수 - 1 개 만큼의 간선이 선택되면 MST가 완성된 것이다.

서로 다른 두 정점의 부모노드가 동일한 경우에 정점을 연결하면 순환이 발생하게 된다.
"""
import heapq
import sys
f_input = sys.stdin.readline


def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]


def union_parent(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


V, E = map(int, f_input().split())

parent = dict()
for i in range(1, V + 1):
    parent[i] = i
edges = list()
for _ in range(E):
    a, b, cost = map(int, f_input().split())
    heapq.heappush(edges, (cost, a, b))

total_weight = 0
used_edges = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    # is cycle ?
    if find_parent(parent, a) != find_parent(parent, b):
        total_weight += cost
        union_parent(parent, a, b)
        used_edges += 1
    if used_edges == V - 1:
        break

print(total_weight)
