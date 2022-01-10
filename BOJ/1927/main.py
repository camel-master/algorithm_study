"""
BOJ 1927 최소 힙
https://www.acmicpc.net/problem/1927

python에서 제공하는 heapq 모듈을 사용해본다.

시간복잡도
heap.heappush()의 시간복잡도는 O(logN)이다.
heap.heappop()의 시간복잡도는 O(logN)이다.
따라서 N개의 연산이 주어지는 경우 O(NlogN)에 처리할 수 있다.
N의 최대값은 100,000이므로 약 1,660,964번의 연산으로 처리할 수 있
제한시간 1초 안에 문제를 풀 수 있다.

공간복잡도
힙에 데이터를 가장 많이 쌓았을 때는 정수 N개를 가지고 있게 되므로 최대
100,000 * 4 Byte = 0.3 mb의 메모리를 사용하게 된다. 메모리 제한이 128MB이므로
사용가능한 알고리즘이다.
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
heap = list()
for _ in range(N):
    num = int(input().rstrip())
    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
