"""
1240번 문제
최단거리 경로 찾기 문제로 dijkstra algorithm을 사용하여 풀이.
4 5
2 1 2
4 3 2
1 4 3
1 2
1 4
1 3
2 4
2 3

2
5
7
5
7
"""
import heapq


N, M = map(int, input().split())
a_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, dist = map(int, input().split())
    a_list[n1].append([n2, dist])
    a_list[n2].append([n1, dist])
two_nodes = list()
for _ in range(M):
    two_nodes.append(list(map(int, input().split())))
INF = int(1e9)

for nodes in two_nodes:
    dist = [INF] * (N + 1)
    n1, n2 = nodes
    dist[n1] = 0
    heap = list()
    for next_node, weight in a_list[n1]:
        dist[next_node] = weight
        heapq.heappush(heap, (weight, next_node))
    while heap:
        acc_w, node = heapq.heappop(heap)
        if dist[node] < acc_w:
            continue
        for next_node, weight in a_list[node]:
            if dist[next_node] > acc_w + weight:
                dist[next_node] = acc_w + weight
                heapq.heappush(heap, (acc_w + weight, next_node))
    print(dist[n2])
