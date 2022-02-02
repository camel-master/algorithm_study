"""
BOJ 11279 최대 힙
https://www.acmicpc.net/problem/11279

python에서 제공하는 heapq를 사용하여 풀어보자.
import heapq
import sys

f_input = sys.stdin.readline

N = int(f_input())
heap = []
for _ in range(N):
    op = int(f_input())
    if op == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -op)

heap 구조 복습 할겸 직접 구현해보자.
          1
      2        3
   4    5   6     7
8

"""
import heapq
import sys

f_input = sys.stdin.readline

N = int(f_input())
heap = []
for _ in range(N):
    op = int(f_input())
    if op == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -op)

# import sys
#
# f_input = sys.stdin.readline
#
#
# class MyHeap:
#     def __init__(self, src_list):
#         self.heap = src_list
#         self.heapify()
#
#     def heappush(self, data):
#         # heap의 가장 끝에 새로운 데이터를 붙이고
#         self.heap.append(data)
#         # heap 구조로 만들어준다.
#
#         pass
#
#     def heappop(self):
#         res = 0
#         if len(self.heap) != 0:
#             res = self.heap[0]
#             # heap의 가장 끝의 데이터를 가장 앞으로 옮긴다.
#             self.heap[0] = self.heap.pop()
#             # heap 구조로 만들어준다.
#
#         return res
#
#     def heapify(self):
#         # leaf node부터 선택하여 heap 구조로 변경한다.
#         s_idx = len(self.heap)
#         while s_idx > 1:
#             c_node = s_idx
#             while c_node > 1:
#                 parent_node = c_node // 2
#                 if self.heap[c_node - 1] < self.heap[parent_node - 1]:
#                     temp = self.heap[c_node - 1]
#                     self.heap[c_node - 1] = self.heap[parent_node - 1]
#                     self.heap[parent_node - 1] = temp
#                 c_node = parent_node
#             s_idx -= 1
#
#
# heap = list()
# heap = [5, 4, 3, 2, 1]
# my_heap = MyHeap(heap)
# print(my_heap.heap)

