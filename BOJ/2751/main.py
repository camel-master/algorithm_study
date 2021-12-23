"""
BOJ 2751 수 정렬하기 2
리스트에 100만개의 정수타입 데이터를 저장하면 4byte * 1,000,000 = 4,000,000 byte이고
메모리 제한은 268,435,456 byte 이므로 내장 정렬함수를 사용하여도 충분히 처리할 수 있겠다.

예제 입력에 코스트가 많이 발생하는 문제이기 때문에 input() 대신 sys.stdin.readline()을
사용해야 통과 된다.
"""
import heapq
import sys
f_input = sys.stdin.readline

N = int(input())
heap = list()
for _ in range(N):
    heapq.heappush(heap, int(f_input()))
while heap:
    print(heapq.heappop(heap))
