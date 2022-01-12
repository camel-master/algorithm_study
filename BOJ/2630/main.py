"""
BOJ 2630 색종이 만들기
https://www.acmicpc.net/problem/2630

N x N 의 종이가 모두 동일한 색인지 확인하여
동일한 색인 경우 하나의 색종이로 간주한다.
다른 색이 하나라도 있는 경우는 4분할 하여
분할 된 각 정사각형이 동일한 색으로만 구성되어 있는지
확인한다.

시간복잡도
O(N^2 * K) N의 max는 128이므로 128 * 128 * 7 = 114,688번의 연산으로
제한 시간 1초를 충분히 통과할 수 있다.

공간복잡도
색종이 정보를 저장해야하므로 최대로 사용하는 저장공간은 O(N^2)이다. 따라서
필요로 하는 메모리는 최대 16kb로 메모리 제한 128MB를 통과할 수 있다.

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
"""
import sys
f_input = sys.stdin.readline


def get_square_color(cp, sr, sc, n, cnt):
    if n == 1:
        if cp[sr][sc] == 0:
            cnt[0] += 1
        else:
            cnt[1] += 1
        return

    first_val = cp[sr][sc]
    is_all_same = True
    for r in range(sr, sr + n):
        for c in range(sc, sc + n):
            if cp[r][c] != first_val:
                is_all_same = False
                break
        if not is_all_same:
            break

    if is_all_same:
        if first_val == 0:
            cnt[0] += 1
        else:
            cnt[1] += 1
    else:
        mid = n // 2
        # 4분할 하여 재귀 호출
        get_square_color(cp, sr, sc, mid, cnt)
        get_square_color(cp, sr, sc + mid, mid, cnt)
        get_square_color(cp, sr + mid, sc, mid, cnt)
        get_square_color(cp, sr + mid, sc + mid, mid, cnt)


N = int(f_input())
cnt = [0, 0]
colored_paper = [list(map(int, f_input().rstrip().split())) for _ in range(N)]

get_square_color(colored_paper, 0, 0, N, cnt)
for color_cnt in cnt:
    print(color_cnt)
