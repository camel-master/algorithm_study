"""
BOJ 11866 요세푸스 문제 0
https://www.acmicpc.net/problem/11866

deque.remove() 의 시간복잡도는 O(n)이다.
1 <= N <= 1,000 이므로 O(N) 알고리즘을 작성하여도 풀이가 가능하다.
다면 여기서는 데이터를 딕셔너리 형태로 관리하는 별도의 Class를 작성하여
시간복잡도를 줄여보고자 한다.

추가로 deque를 사용했을 때 순환하며 인덱싱 하는 기법을 익히도록 한다.

S     P
1, 2, 3, 4, 5, 6, 7
3

      S     P
1, 2, 4, 5, 6, 7
3, 6

   P        S
1, 2, 4, 5, 7
3, 6, 2

   S     P
1, 4, 5, 7
3, 6, 2, 7

S     P
1, 4, 5
3, 6, 2, 7, 5

S
P
1, 4
3, 6, 2, 7, 5, 1

S
P
4
3, 6, 2, 7, 5, 1, 4
"""
from collections import defaultdict
from collections import deque
import sys

f_input = sys.stdin.readline


# N, K = map(int, f_input().split())
# {index: (pre_index, next_index)}
for i in range(1, 7):
