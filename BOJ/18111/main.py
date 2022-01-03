"""
BOJ 18111 마인크래프트
https://www.acmicpc.net/problem/18111

각 높이에 해당하는 블럭의 좌표들을 저장한다.
각 높이별로 몇개의 좌표가 있는지 확인한다.
가장 낮은 높이의 좌표와 가장 높은 높이의 좌표를 확인한다.
인벤토리에서 블럭을 하나씩 꺼내 가장 낮은 높이의 좌표로 부터 블럭을 채우는 작업을 실시한다.
가장 높은 높이의 좌표로 부터는 블럭을 제거하여 인벤토리에 넣는 작업을 실시한다.
만약 최저 높이와 최고높이가 인접하게 되면 위의 작업 중 시간이 적게 걸리는 작업을 선택한다.

가장 낮은 곳에 위치한 블럭의 높이를 X라 하고, 모든 X보다 높은 좌표들에 대해 좌표의 높이 - X를 sum_X에 누적하여
더한다.
sum_X * 2 = 블럭을 뽑아서 인벤토리에 넣어 평탄화 하는데 걸리는 가장 긴 시간

가장 높은 곳에 위치한 블럭의 높이를 Y라고 하면
(Y - X) * N * M - sum_X = 인벤토리에서 블럭을 가져와 채우는데 걸리는 가장 긴 시간

가장 낮은 높이의 블럭기준 채우기로 평탄화 작업을 진행 했을 때와 가장 높은 높이의 블럭기준 빼기로 평탄화 작업을 진행했을 때의
시간 차이를 비교하여 유리한 쪽으로 진행하도록 알고리즘을 작성해보도록 하자.
최저 높이 블럭 기준 채우기 시 최고 높이에서 뽑아내기로 시작했을 때 걸리는 max 시간에서 얼마나 단축되나? = sT_1
최고 높이 블럭 기준 뽑기 시 최저 높이에서 채우기로 시작했을 때 걸리는 max 시간에서 얼마나 단축되나? = sT_2
sT_1과 sT_2 중 짧은 시간을 선택 한다. 만약 sT_1 == sT_2이면 낮은 높이의 블럭을 채우는 쪽을 선택한다.

0 ~ 256 사이의 높이별로 블럭이 각 층마다 몇개가 있는지 저장해놓는다.
0부터 시작해서 blcok_cnt < N * M 인 높이를 찾고 이것을 빈 블럭이 있는 가장 낮은 높이로 잡는다. (min_height)
256부터 시작해서 block_cnt > 0인 높이를 찾고 이것을 빈 블럭이 있는 가장 높은 높이로 잡는다. (max_height)

fill_cost(min_height) = 가장 낮은 높이의 빈 블럭을 채우는데 필요한 비용
pull_cost(max_height) = 가장 높은 높이의 블럭을 빼는데 필요한 비용
if fill_cost(min_height) < pull_cost(max_height) and B >= block_count then
    B = B - block_count
    min_height = min_height + 1
else if fill_cost(min_height) > pull_cost(max_height) then
    B = B + block_count
    max_height = max_height - 1
else:
    print(max_height)

------------------------------------------------------------------------------------------------
N * M 높이 를 각 높이별로 개수를 파악한다.

64 64 64 64
64 64 64 64
64 64 64 63

위와 같이 높이가 주어진 경우 64 높이의 좌표는 11개이고 63은 1개이다.
이 데이터를 높이 기준으로 정렬한다.
{63: 1, 64: 11}
가장 낮은 높이에서 그 다음 높이 사이에 비어있는 블럭 수는?


1 1 3 3
1 3 3 5
3 3 5 5
3 5 6 7
(1, 3), (3, 7), (5, 4), (6, 1), (7, 1)

0 ~ (1 - 1) 에 해당하는 빈공간은 모두 0 = 0
1 ~ (3 - 1) 에 해당하는 빈공간은 모두 0 + 1 = 1
3 ~ (7 - 1) 에 해당하는 빈공간은 모두 1 + 3 = 4
5 ~ (6 - 1) 에 해당하는 빈공간은 모두 4 + 4 = 8
6 ~ (7 - 1) 에 해당하는 빈공간은 모두 8 + 1 = 9
7 에 해당하는 빈공간은 9 + 1 = 10

더 작은 사이즈로 테스트 해보자.
0 1 2
1 2 3
2 3 4
(0, 1), (1, 2), (2, 3), (3, 2), (4, 1)
0 ~ 0: 1
1 ~ 1: 1 + 2 = 3
2 ~ 2: 3 + 3 = 6
3 ~ 3: 6 + 2 = 8
4 ~ 256: 8 + 1 = 9


64 64 64 64
64 64 64 64
64 64 64 63
(63, 1), (64, 11)
0 ~ 62: 0
63 ~ 63: 0 + 1
64 ~ 256: 1 + 11 = 12

"""
import sys
f_input = sys.stdin.readline

N, M, B = map(int, f_input().split())
# stacked block info
s_b_info = list()
for _ in range(N):
    s_b_info.append(list(map(int, f_input().rstrip().split())))

s_b_height = dict()
s_b_cnt = dict()
for r in range(N):
    for c in range(M):
        floor = s_b_info[r][c]
        try:
            s_b_height[floor] += 1
        except KeyError:
            s_b_height[floor] = 1

max_height = max(s_b_height.keys())
for i in range(max_height, -1, -1):
    if i == max_height:
        s_b_cnt[i] = s_b_height[i]
    else:
        try:
            s_b_cnt[i] = s_b_cnt[i + 1] + s_b_height[i]
        except KeyError:
            s_b_cnt[i] = s_b_cnt[i + 1]

# for floor in range(257):
#     for r in range(N):
#         for c in range(M):
#             if s_b_info[r][c] >= floor:
#                 try:
#                     s_b_cnt[floor] += 1
#                 except KeyError:
#                     s_b_cnt[floor] = 1


# 블럭을 끼워 넣는 연산은 다음 층의 높이에 몇개의 블럭이 있는지 확인해야 가능하고
# 블럭을 빼는 연산은 아무 조건 없이 가능하다.
acc_time = 0
l_side_idx = 0
r_side_idx = max(s_b_cnt.keys())
while l_side_idx < r_side_idx:
    fill_cost = N * M - s_b_cnt[l_side_idx + 1]
    pull_cost = s_b_cnt[r_side_idx] * 2

    if pull_cost >= fill_cost and B >= fill_cost:
        B -= fill_cost
        l_side_idx += 1
        acc_time += fill_cost
    else:
        B += s_b_cnt[r_side_idx]
        r_side_idx -= 1
        acc_time += pull_cost

print(acc_time, r_side_idx)
