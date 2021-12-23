"""
BOJ 2775 부녀회장이 될테야
k층, n호에 사는 사람의 수

0층 1호 = 1명
0층 2호 = 2명
0층 3호 = 3명
1층 1호 = 1명
1층 2호 = 3명
1층 3호 = 6명

단순히 0층 1호 부터 초기값을 잡고 원하는 층과 호가 될 때 까지 데이터를 작성하면
O(k * n)으로 해를 구할 수 있다.
"""
import sys
f_input = sys.stdin.readline

T = int(f_input())
for _ in range(T):
    k = int(f_input())
    n = int(f_input())
    people_cnt = [[i for i in range(0, n + 1)]]
    for floor in range(1, k + 1):
        people_cnt.append([0] * (n + 1))
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            people_cnt[floor][room] = sum(people_cnt[floor-1][:room + 1])
    print(people_cnt[-1][-1])