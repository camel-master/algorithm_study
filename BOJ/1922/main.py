"""
BOJ 1922 네트워크 연결
https://www.acmicpc.net/problem/1922

최저 비용으로 모든 노드를 연결하는 네트워크를 구성하는 문제로
Minimal Spanning Tree 문제이다.
크루스칼 알고리즘을 사용하여 이 문제를 해결해보고자 한다.
크르수칼 알고리즘의 시간복잡도는 O(E log E)이므로
최대 약 100000 * log 1000000 = 1,600,000 번의 연산으로
결과를 얻을 수 있으므로 시간제한을 통과할 수 있다.

각 노드의 부모노드 정보를 가지고 있어야 하므로 최대 1000 * 4 Byte = 약 0.00038MB 공간 필요
간선 및 가중치 정보를 모두 가지고 있어야 하므로 최대 100000 * 3 * 4 Byte = 약 1.14MB
그러므로 메모리 제한도 통과할 수 있다.
"""
import heapq
import sys

f_input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(f_input())
M = int(f_input())
parent = [0]
for i in range(1, N + 1):
    parent.append(i)
edges = []
result = 0
for _ in range(M):
    a, b, cost = map(int, f_input().rstrip().split())
    heapq.heappush(edges, (cost, a, b))
while edges:
    cost, a, b = heapq.heappop(edges)
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa != pb:
        union_parent(parent, pa, pb)
        result += cost

print(result)
