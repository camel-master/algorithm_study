"""
BOJ 7662 이중 우선순위 큐
https://www.acmicpc.net/problem/7662

두 개의 heap을 사용하여 해결해본다.
min heap과 max heap을 각각 선언하고
데이터 삽입 시 두 heap에 동시에 데이터를 쌓는다.
D -1인 경우 최소 힙을 heappop
D 1인 경우 최대 힙을 heappop 한다.
min_heap[0] <= -max_heap[0] 라면 min, max 값이 존재한다.
 min_heap[0] > -max_heap[0] 이면 데이터가 없는 것이다.
if min_heap[0] == -max_heap[0] then heappop(min_heap), heappop(max_heap)


별도의 삭제여부 테이블을 사용하여 min_heap과 max_heap을 동기화 시킨다.
"""
# import heapq
# import sys
#
# f_input = sys.stdin.readline
#
#
# min_heap = list()
# max_heap = list()
#
# T = int(f_input())
# for _ in range(T):
#     k = int(f_input())
#     for _ in range(k):
#         data = f_input().rstrip().split()
#         op = data[0]
#         n = int(data[1])
#         if op == 'I':
#             heapq.heappush(min_heap, n)
#             heapq.heappush(max_heap, -n)
#         if op == 'D':
#             if len(min_heap) == 0 or len(max_heap) == 0:
#                 continue
#             if n == -1: # 최소값 삭제
#                 deleted_n = heapq.heappop(min_heap)
#                 max_heap.remove(-deleted_n)
#                 # heapq.heapify(max_heap)
#             else:
#                 deleted_n = heapq.heappop(max_heap)
#                 min_heap.remove(-deleted_n)
#                 # heapq.heapify(min_heap)
#
#     if len(min_heap) == 0 or len(max_heap) == 0:
#         print('EMPTY')
#     else:
#         print(-max_heap[0], min_heap[0])


# import heapq
# import sys
#
# f_input = sys.stdin.readline
#
# min_heap = list()
# max_heap = list()
#
# T = int(f_input())
# for _ in range(T):
#     k = int(f_input())
#     for _ in range(k):
#         data = f_input().rstrip().split()
#         op = data[0]
#         n = int(data[1])
#         if op == 'I':
#             temp = list()
#             try:
#                 while -max_heap[0] == min_heap[0]:
#                     temp.append(heapq.heappop(min_heap))
#             except IndexError:
#                 pass
#             if temp:
#                 min_heap = temp
#                 max_heap = [-i for i in temp]
#                 heapq.heapify(min_heap)
#                 heapq.heapify(max_heap)
#             heapq.heappush(min_heap, n)
#             heapq.heappush(max_heap, -n)
#         elif op == 'D':
#             temp = list()
#             if n == -1:
#                 try:
#                     while -max_heap[0] == min_heap[0]:
#                         temp.append(heapq.heappop(min_heap))
#                 except IndexError:
#                     pass
#                 if temp:
#                     min_heap = temp
#                     heapq.heapify(min_heap)
#                     heapq.heappop(min_heap)
#                     heapq.heappop(max_heap)
#                 else:
#                     if min_heap:
#                         heapq.heappop(min_heap)
#             elif n == 1:
#                 try:
#                     while -max_heap[0] == min_heap[0]:
#                         temp.append(heapq.heappop(max_heap))
#                 except IndexError:
#                     pass
#                 if temp:
#                     max_heap = temp
#                     heapq.heapify(max_heap)
#                     heapq.heappop(min_heap)
#                     heapq.heappop(max_heap)
#                 else:
#                     if max_heap:
#                         heapq.heappop(max_heap)
#     if min_heap:
#         print(-max_heap[0], min_heap[0])
#     else:
#         print('EMPTY')


import sys
from heapq import heappop, heappush

f_input = sys.stdin.readline

t = int(f_input())
for i in range(t):
    max_heap = []
    min_heap = []
    k = int(f_input())
    delete_yn = [0] * k

    for j in range(k):
        l, n = f_input().split()
        n = int(n)

        if l == 'I':
            heappush(max_heap, (-n, j))
            heappush(min_heap, (n, j))

            delete_yn[j] = 1
        else:
            if n == -1:
                while min_heap and delete_yn[min_heap[0][1]] == 0:
                    heappop(min_heap)

                if min_heap:
                    delete_yn[min_heap[0][1]] = 0
                    heappop(min_heap)
            else:
                while max_heap and delete_yn[max_heap[0][1]] == 0:
                    heappop(max_heap)

                if max_heap:
                    delete_yn[max_heap[0][1]] = 0
                    heappop(max_heap)

    while max_heap and delete_yn[max_heap[0][1]] == 0:
        heappop(max_heap)
    while min_heap and delete_yn[min_heap[0][1]] == 0:
        heappop(min_heap)

    if not max_heap and not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
