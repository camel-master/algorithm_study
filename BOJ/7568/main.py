"""
BOJ 7568 덩치
https://www.acmicpc.net/problem/7568

한 사람의 덩치를 (몸무게, 키)로 표현한다.
두 사람이 있을 때 몸무게와 키가 모두 또 다른 한명을 초과할 때는 덩치가 크다고 한다.
위와 다르게 키나 몸무게 둘 중 하나만 다른 한명을 초과할 때는 덩치의 크고 작음을 구분할 수 없다.

2 <= N <= 50

입력 데이터가 다음과 같을 때
5
55 185
58 183
88 186
60 175
46 155

자신 보다 덩치가 큰 사람이 몇명인지를 찾아 덩치큰 사람 + 1이 현재 확인 중인 사람의 등수가 된다.
따라서 N명에 대해 모두 등수를 확인하도록 하면 시간복잡도는 O(n^2)가 된다.
"""
import sys
f_input = sys.stdin.readline
N = int(f_input())

size_list = list()
for _ in range(N):
    size_list.append(tuple(map(int, f_input().rstrip().split())))

for i in range(N):
    bigger_cnt = 0
    for j in range(N):
        if i != j:
            if size_list[i][0] < size_list[j][0] and size_list[i][1] < size_list[j][1]:
                bigger_cnt += 1
    if i == N - 1:
        print(bigger_cnt + 1)
    else:
        print(bigger_cnt + 1, end=' ')
