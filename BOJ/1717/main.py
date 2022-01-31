"""
BOJ 1717 집합의 표현
https://www.acmicpc.net/problem/1717

Union-Find 연산을 통해 풀어보자.
"""
import sys

f_input = sys.stdin.readline


def find_parent(parent, elem):
    if parent[elem] == elem:
        return elem
    else:
        parent[elem] = find_parent(parent, parent[elem])

    return parent[elem]


def union_parent(parent, pa, pb):
    if pa > pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


n, m = map(int, f_input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, f_input().split())
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if op == 0:
        union_parent(parent, pa, pb)
    else:
        if pa == pb:
            print('YES')
        else:
            print('NO')
