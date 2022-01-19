"""
BOJ 7576 토마토
2 <= N, M <= 1,000
익은 토마토를 queue에 넣고 BFS를 돌리려서 최소 일 수를 구하고자한다.

시간복잡도
BFS의 시간복잡도는 O(V + E)이므로 최대 1,000,000 + (1,000,000 + 1,000,000)으로
약 3,000,000 번의 연산으로 처리할 수 있기에 시간 제한 1초를 만족할 수 있다.

공간복잡도
실제 상자와 걸리는 날 수를 저장할 데이터 공간이 필요하다. 1,000 * 1,000 size의 상자라
할 때, 각 칸마다 정수가 저장되어야 하므로
1000 * 1000 * 4 byte = 4,000,000 byte 만큼 필요하고
동일한 크기의 날 수를 저장할 공간이 필요하므로 총 8,000,000 byte = 약 7.6MB로
메모리 제한 256MB를 통과할 수 있다.



참고할 코드
import sys
from collections import deque
input = sys.stdin.readline


def solve():
    m, n = map(int, input().split())
    tomato = []
    haveto = 0
    tmt = deque()
    for i in range(n):
        tomato.append(input().split())
        for j in range(m):
            if tomato[i][j] == '0':
                haveto += 1
            elif tomato[i][j] == '1':
                tmt.append((i, j))
    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            x, y = tmt.popleft()
            if x > 0 and tomato[x-1][y] == '0':
                tomato[x-1][y] = 1
                tmt.append((x-1, y))
                haveto -= 1
            if y > 0 and tomato[x][y-1] == '0':
                tomato[x][y-1] = 1
                tmt.append((x, y-1))
                haveto -= 1
            if x < n-1 and tomato[x+1][y] == '0':
                tomato[x+1][y] = 1
                tmt.append((x+1, y))
                haveto -= 1
            if y < m-1 and tomato[x][y+1] == '0':
                tomato[x][y+1] = 1
                tmt.append((x, y+1))
                haveto -= 1
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    solve()
"""
from collections import deque
import sys

f_input = sys.stdin.readline

M, N = map(int, f_input().rstrip().split())
tomato_box = []
queue = deque()
days = [[-1] * (M + 2) for _ in range(N + 2)]
for i in range(N + 2):
    if i == 0 or i == N + 1:
        tomato_box.append([-1] * (M + 2))
    else:
        tomato_box.append([-1])
        row = list(map(int, f_input().rstrip().split()))
        for j in range(1, len(row) + 1):
            tomato_box[-1].append(row[j-1])
            if row[j-1] == 1:
                queue.append((i, j))
                days[i][j] += 1
        tomato_box[-1].append(-1)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
max_spent_days = 0
while queue:
    c_tomato_y, c_tomato_x = queue.popleft()
    for d in range(4):
        n_tomato_y = c_tomato_y + dy[d]
        n_tomato_x = c_tomato_x + dx[d]
        if tomato_box[n_tomato_y][n_tomato_x] == 0 and days[n_tomato_y][n_tomato_x] == -1:
            queue.append((n_tomato_y, n_tomato_x))
            days[n_tomato_y][n_tomato_x] = days[c_tomato_y][c_tomato_x] + 1
            if max_spent_days < days[n_tomato_y][n_tomato_x]:
                max_spent_days = days[n_tomato_y][n_tomato_x]

is_unripe = False
for i in range(N + 1):
    for j in range(M + 1):
        if tomato_box[i][j] == 0 and days[i][j] == -1:
            is_unripe = True
            break
    if is_unripe:
        break
if is_unripe:
    print(-1)
else:
    print(max_spent_days)
