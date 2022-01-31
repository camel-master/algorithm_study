"""
BOJ 5073 삼각형과 세 변
https://www.acmicpc.net/problem/5073

삼각형을 이루기 위한 조건은 두 변의 합이 남은 한 변보다 길어야 한다는 것이다.
"""
from collections import Counter
import sys

f_input = sys.stdin.readline
while True:
    e1, e2, e3 = map(int, f_input().split())
    edges_cnt = Counter([e1, e2, e3])
    if edges_cnt[0] == 3:
        break
    else:
        if len(edges_cnt) == 1:
            print('Equilateral')
        else:
            if e1 >= e2 + e3 or e2 >= e1 + e3 or e3 >= e2 + e1:
                print('Invalid')
            elif len(edges_cnt) == 2:
                print('Isosceles')
            else:
                print('Scalene')
