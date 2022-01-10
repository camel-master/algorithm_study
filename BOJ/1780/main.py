"""
BOJ 1780 종이의 개수
https://www.acmicpc.net/problem/1780

3**7 = 2187
naive한 풀이를 생각해보자.
n의 최대 값은 2187이므로 n = 2187이라 가정한다.
n x n 행렬의 모든 요소가 동일한 요소인지 확인하기 위해서는 2187 * 2187번의 연산이 필요하다.
만약 마지막 1개가 다른 경우 총 4,782,969번의 탐색이 필요하다.

이제 729 * 729 크기의 행렬을 총 9개 탐색해야한다. 모든 탐색에 소요되는 연산 회수는 4,782,969 이다.

이제 243 * 243 크기의 행렬을 총 27개 탐색해야 한다. 모든 탐색에 소요되는 연산 회수는 4,782,969 이다.

81, 27, 9, 3

시간복잡도
즉, 최악의 경우 4,782,969 * 7 = 33,480,783 번 연산 안에 모두 처리할 수 있게 된다.
시간제한은 2초이므로 3천3백만번 연산은 충분히 처리할 수 있으므로 단순하게 n을 3등분 하여 처리하는 알고리즘은
사용할 수 있다.

공간복잡도
n = 2187 일때 n * n * 4 = 약 18MB이므로 사용할 수 있는 알고리즘이다.

현재 확인하는 범위내에 숫자의 종류가 2종류 이상인 경우 9조각으로 나눠서 다시 탐색하는 기능을
재귀적으로 구현한다.

"""
from collections import defaultdict
import sys
input = sys.stdin.readline


def get_papers_count(matrix, sr, sc, N, cnt):
    if N == 1:
        if matrix[sr][sc] == -1:
            cnt[-1] += 1
            return
        elif matrix[sr][sc] == 0:
            cnt[0] += 1
            return
        elif matrix[sr][sc] == 1:
            cnt[1] += 1
            return
    elems = defaultdict(int)
    split_yn = False
    for r in range(sr, sr + N):
        for c in range(sc, sc + N):
            elems[matrix[r][c]] += 1
            if len(elems.items()) > 1:
                split_yn = True
                break
        if split_yn:
            break
    if not split_yn:
        keys = list(elems.keys())
        cnt[keys[0]] += 1
        return
    else:
        for i in range(sr, sr + N, N // 3):
            for j in range(sc, sc + N, N // 3):
                get_papers_count(matrix, i, j, N // 3, cnt)

N = int(input().rstrip())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

cnt = {-1: 0, 0: 0, 1: 0}
get_papers_count(matrix, 0, 0, N, cnt)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
