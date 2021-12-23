"""
BOJ 2146 카드2
acmicpc.net/problem/2164

순차적으로 정렬된 1 ~ N 까지의 카드가 있다.
(N - 1) * 2
N == 4
1234
234
342
42
24
4

N == 5
12345
2345
3452
452
524
24
42
2

N == 6
123456
 23456
 34562
  4562
  5624
   624
   246
    46
    64
     4

N == 7
1234567
234567
345672
45672
56724
6724
7246
246
462
62
26
6
"""
from collections import deque


N = int(input())
queue = deque(i for i in range(1, N + 1))
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])
