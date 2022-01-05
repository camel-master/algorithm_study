"""
BOJ 1389 케빈 베이컨의 6단계 법칙
https://www.acmicpc.net/problem/1389

N명의 사람들 간에 M의 관계가 있다.
한 명이 다른 모든 사람들 까지 몇 단계를 거쳐야 알 수 있는지 확인해야 하므로
다익스트라 알고리즘을 사용하고자 한다.
각 모든 사람들을 시작 노드로 하여 다익스트라 알고리즘을 실행 한 후
거리가 가장 짧은 것을 취한다.
O(N log M * N) = 100 * 12.29 * 100 = 122,900
최대 122,900번의 연산으로 처리 가능하므로 시간 복잡도를 통과할 수 있다.

다익스트라 알고리즘 수행을 위한 인접리스트를 작성했을 때 최대 크기는
5000 * 2 * 4 byte = 39 KB로 처리 가능.
"""
import heapq
import sys
f_input = sys.stdin.readline


def dijkstra(s_node):
    # visited_nodes = list()
    lowest_cost_table[s_node] = 0
    priority_queue = list()
    heapq.heappush(priority_queue, (0, s_node))  # the tuple's values consist of cost and node
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        # if from_node in visited_nodes:
        if lowest_cost_table[current_node] < current_cost:
            continue
        # visited_nodes.append(from_node)
        for next_node, edge_weight in relations[current_node]:
            if lowest_cost_table[next_node] > current_cost + edge_weight:
                lowest_cost_table[next_node] = current_cost + edge_weight
                heapq.heappush(priority_queue, (lowest_cost_table[next_node], next_node))


N, M = map(int, f_input().rstrip().split())
relations = [[] for _ in range(N + 1)]
for _ in range(M):
    p1, p2 = map(int, f_input().rstrip().split())
    relations[p1].append((p2, 1))
    relations[p2].append((p1, 1))

level_by_person = list()
INF = int(1e9)
for i in range(1, N + 1):
    # lowest_cost_table declaring and initializing
    lowest_cost_table = [INF] * (N + 1)
    dijkstra(i)
    sum_lct = 0
    for j in range(1, len(lowest_cost_table)):
        lct_val = lowest_cost_table[j]
        if i != j:    # 자기 자신으로 가는 것은 무시
            sum_lct += lct_val
    level_by_person.append((i, sum_lct))
level_by_person.sort(key=lambda x: x[1])
print(level_by_person[0][0])
