"""
BOJ 2252 줄 세우기

관계를 통해서 정렬해야 하는 경우 위상 정렬을 사용한다.
각 학생마다 자기 보다 작은 학생 몇명과 연결 되었는지를 기록한다.

"""
from collections import deque
import sys

f_input = sys.stdin.readline

N, M = map(int, f_input().split())

# 진입 간선 수를 카운팅한다. 방향은 작은 학생 -> 큰 학생이다.
students_conn_cnt = [0] * (N + 1)
relations = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, f_input().split())
    students_conn_cnt[B] += 1
    relations[A].append(B)

queue = deque()
for i in range(1, len(students_conn_cnt)):
    if students_conn_cnt[i] == 0:
        queue.append(i)

res = []
while queue:
    curr_student = queue.popleft()
    res.append(curr_student)
    for conn_student in relations[curr_student]:
        if students_conn_cnt[conn_student] > 0:
            students_conn_cnt[conn_student] -= 1
            if students_conn_cnt[conn_student] == 0:
                queue.append(conn_student)

print(*res)


# from collections import deque
# from collections import defaultdict
# import sys
#
# f_input = sys.stdin.readline
#
# # 진입 간선 수를 카운팅하여 딕셔너리에 넣는다.
# students_conn_cnt = defaultdict(int)
# relations = defaultdict(list)
# N, M = map(int, f_input().split())
# for _ in range(M):
#     A, B = map(int, f_input().split())
#     students_conn_cnt[A]
#     students_conn_cnt[B] += 1
#     relations[A].append(B)
#
# # 진입 간선 수가 0인 학생들을 queue에 넣는다.
# queue = deque()
# for item in students_conn_cnt.items():
#     if item[1] == 0:
#         queue.append(item[0])
#
# res = []
# # queue가 빌 때까지 다음을 반복
# while queue:
#     curr_student = queue.popleft()
#     res.append(curr_student)
#     for conn_student in relations[curr_student]:
#         if students_conn_cnt[conn_student] > 0:
#             students_conn_cnt[conn_student] -= 1
#             if students_conn_cnt[conn_student] == 0:
#                 queue.append(conn_student)
#
# print(*res)
