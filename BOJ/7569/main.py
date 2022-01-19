"""
BOJ 7569 토마토
https://www.acmicpc.net/problem/7569

BFS로 완전탐색을 진행하여 풀고자 한다.
주어지는 토마토 상자 정보를 3차원 리스트로 변경한다.

빈공간의 수 empty_spaces 를 확인한다.
익은 토마토의 수 ripe_tomatoes 를 확인한다.

방문 내역 3차원 리스트의 모든 요소를 -1로 초기화 한다.
익은 토마토의 좌표를 모두 큐에 넣고 BFS를 시작한다.
방문내역을 기록할 때 다음 연결된 노드로 넘어가는 현재 방문내역 + 1로 값을 업데이트 한다.
업데이트 할 때마다 maximum 값을 업데이트 해나간다. (maximum의 초기값은 0이다.)


최대 노드의 개수는 100 * 100 * 100 = 1,000,000 개이다.
최대 간선의 개수는 (100 - 1) * 100 * 2 * 100 + 100 * (100 - 1) = 1,989,900 개이다.
BFS의 시간복잡도는 O(V + E) 이므로 최대 약 300만회 연산으로 결과를 구할 수 있기 떄문에
사용할 수 있는 알고리즘이다.

3차원 리스트로 상자 구조를 나타내야 하므로 100 * 100 * 100 * 4 byte = 3.8 mb로
제한된 256mb 이하를 사용하므로 사용할 수 있는 알고리즘이다.

2 2 2
1 1
0 -1
0 -1
-1 0

2 2 2
1 1
0 0
0 0
0 0

참고할 코드
import sys
input = sys.stdin.readline

def solution():

    n, m, h = map(int, input().split())
    board = [[[*map(int, input().split())] for _ in range(m)] for _ in range(h)]
    cnt = 0
    tomatoes = []
    depth = -1

    for k in range(h):
        for i in range(m):
            for j in range(n):
                if board[k][i][j] == 0:
                    cnt += 1
                elif board[k][i][j] == 1:
                    tomatoes.append((k, i, j))

    while tomatoes:
        depth += 1
        temp = []
        for k, i, j in tomatoes:
            if k > 0 and board[k-1][i][j] == 0:
                board[k-1][i][j] = 1
                temp.append((k-1,i,j))
            if i > 0 and board[k][i-1][j] == 0:
                board[k][i-1][j] = 1
                temp.append((k,i-1,j))
            if j > 0 and board[k][i][j-1] == 0:
                board[k][i][j-1] = 1
                temp.append((k,i,j-1))
            if k < h-1 and board[k+1][i][j] == 0:
                board[k+1][i][j] = 1
                temp.append((k+1,i,j))
            if i < m-1 and board[k][i+1][j] == 0:
                board[k][i+1][j] = 1
                temp.append((k,i+1,j))
            if j < n-1 and board[k][i][j+1] == 0:
                board[k][i][j+1] = 1
                temp.append((k,i,j+1))
        cnt -= len(temp)
        tomatoes = temp

    return -1 if cnt else depth

print(solution())
"""
from collections import deque
import sys

f_input = sys.stdin.readline

M, N, H = map(int, f_input().rstrip().split())
# BFS 범위를 1 ~ M, N, H로 잡아 잘못된 인덱스 접근을 막기 위해 각 축의 양 끝에 한 칸씩을 더해서 리스트를 생성한다.
tomato_boxes = [[[-1] * (M + 2) for _ in range(N + 2)] for _ in range(H + 2)]

for z in range(1, H + 1):
    for y in range(1, N + 1):
        row = list(map(int, f_input().rstrip().split()))
        for x in range(1, len(row) + 1):
            tomato_boxes[z][y][x] = row[x-1]

# 익은 토마토를 모두 큐에 넣는다. 좌표는 (z, y, x) 형태다
queue = deque()
days = [[[-1] * (M + 2) for _ in range(N + 2)] for _ in range(H + 2)]
for z in range(1, H + 1):
    for y in range(1, N + 1):
        for x in range(1, M + 1):
            if tomato_boxes[z][y][x] == 1:
                queue.append((z, y, x))
                days[z][y][x] += 1

# print(tomato_boxes)
# print(queue)
# print(days)

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
spending_days = 0
while queue:
    c_tomato_z, c_tomato_y, c_tomato_x = queue.popleft()
    for d in range(6):
        n_tomato_z = c_tomato_z + dz[d]
        n_tomato_y = c_tomato_y + dy[d]
        n_tomato_x = c_tomato_x + dx[d]
        # 다음 위치에 있는 토마토가 익지 않은 토마토인 경우
        if tomato_boxes[n_tomato_z][n_tomato_y][n_tomato_x] == 0 and days[n_tomato_z][n_tomato_y][n_tomato_x] == -1:
            queue.append((n_tomato_z, n_tomato_y, n_tomato_x))
            days[n_tomato_z][n_tomato_y][n_tomato_x] = days[c_tomato_z][c_tomato_y][c_tomato_x] + 1
            if days[n_tomato_z][n_tomato_y][n_tomato_x] > spending_days:
                spending_days = days[n_tomato_z][n_tomato_y][n_tomato_x]

# 한번도 방문하지 못한 노드가 있으면 -1을
is_unripe = False
for z in range(1, H + 1):
    for y in range(1, N + 1):
        for x in range(1, M + 1):
            if days[z][y][x] == -1 and tomato_boxes[z][y][x] == 0:
                is_unripe = True
                break
        if is_unripe:
            break
    if is_unripe:
        break

if is_unripe:
    print(-1)
else:
    print(spending_days)
