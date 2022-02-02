"""
BOJ 12865 평범한 배낭
https://www.acmicpc.net/problem/12865

4 7
6 13
4 8
3 6
5 12

100 100
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1

combination으로 모든 물건의 조합을 확인하면 시간 제한을 만족할 수 없게 된다.
n!/(n-m)!*m! = 100!/50!*50! = (응, 너 관뚜껑 닫을 때까지 해도 안돼)

DP로 접근해보자.
무게를 초과하지 않는 가치의 최대 값을 찾아야 한다.
f(n): 물건들의 가치 최대 합 중 무게가 K 이하인 것

다음의 입력이 주어질 때 데이터를 정렬한다.
4 7
6 13
4 8
3 6
5 12

첫번 째 정렬 조건 = 무게 오름차순
두번 쨰 정렬 조건 = 가치 내림차순
3 6
4 8
5 12
6 13

if n-1 번째 물건 까지의 무게의 최대 합 + n번째 물건의 무게 > K then
    if n-1 번째 물건 까지 가치 최대 합 > n번째 물건의 가치:
        W[n] = W[n-1]
        V[n] = V[n-1]
    else:
        W[n] = weights[n]
        V[n] = values[n]
else:
    W[n] = W[n-1] + weights[n]
    V[n] = V[n-1] + values[n]

W  3  7  7  7
V  6 14 14 14

냅색 알고리즘... 모르면 틀려야지

test case 1 (expected: 264)
7 19
9 89
8 80
1 32
6 68
2 74
3 42
7 2

test case 2 (expected: 23)
6 9
3 6
2 7
4 6
4 2
4 10
1 5

test case 3 (expected: 31)
9 10
1 8
5 10
4 10
2 6
4 5
4 7
3 7
4 7
1 4

test case 4 (expected: 26)
6 7
3 7
3 10
1 6
2 7
3 5
2 9

test case 5 (expected: 19)
7 9
3 6
2 4
2 5
3 4
1 3
4 1
2 4

test case 6 (expected: 20)
7 7
1 4
3 1
3 6
2 6
3 8
3 4
2 6

test case 7 (expected: 16)
5 9
2 4
1 3
3 5
4 8
2 1

test case 8 (expected: 31)
8 9
1 4
2 7
3 10
2 7
2 7
4 8
3 5
4 1

test case 9 (expected: 38)
9 10
4 2
4 9
1 5
1 7
2 8
3 9
2 8
2 6
3 5

test case 10 (expected: 21)
5 7
3 8
1 5
2 7
2 2
2 6

test case 11 (expected: 30)
10 10
1 2
4 9
1 5
4 8
4 1
1 7
3 2
3 7
2 5
5 2

test case 12 (expected: 24)
9 7
1 1
1 4
3 10
2 1
2 7
3 8
3 9
3 3
2 7

test case 13 (expected: 37)
9 9
2 9
1 7
3 10
2 2
3 3
4 9
2 10
2 8
3 2

[참고할 코드 1]
import sys
input=sys.stdin.readline
def sol():
    n,k=map(int,input().split())
    kk=k+1
    bag=dict()
    bag[0]=0
    data=[tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)
    for w,v in data:
        tmp={}
        for vv,ww in bag.items():
            if bag.get(vvv:=vv+v,kk)>(www:=w+ww):
                tmp[vvv]=www
        bag.update(tmp)
    print(max(bag.keys()))
sol()

[참고할 코드 2]
import sys
read = sys.stdin.readline


def dp(n, k):
    dp_dict = {0: 0}
    for _ in range(n):
        new_w, new_v = map(int, read().split())
        temp = {}
        for acc_w, acc_v in dp_dict.items():
            if acc_w + new_w <= k and acc_v + new_v > dp_dict.get(acc_w + new_w, 0):
                temp[acc_w + new_w] = acc_v + new_v
        dp_dict.update(temp)
    return max(dp_dict.values())


N, K = map(int, read().split())
print(dp(N, K))
"""
import sys

f_input = sys.stdin.readline

n, k = map(int, f_input().split())

goods = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    goods.append(list(map(int, f_input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = goods[i][0]
        v = goods[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])

# import sys
#
# f_input = sys.stdin.readline
#
# N, K = map(int, f_input().split())
#
# data = [tuple(map(int, f_input().split())) for _ in range(N)]
# data.sort(key=lambda d: (-d[1], d[0]))
# dp_w = [0] * N
# dp_v = [0] * N
# if data[0][0] <= K:
#     dp_w[0] = data[0][0]
#     dp_v[0] = data[0][1]
#
# for i in range(1, N):
#     if dp_w[i-1] + data[i][0] > K:
#         if dp_v[i-1] > data[i][1]:
#             dp_w[i] = dp_w[i - 1]
#             dp_v[i] = dp_v[i - 1]
#         else:
#             dp_w[i] = data[i][0]
#             dp_v[i] = data[i][1]
#     else:
#         dp_w[i] = dp_w[i - 1] + data[i][0]
#         dp_v[i] = dp_v[i - 1] + data[i][1]
#
# print(dp_v[-1])

# import sys
#
# f_input = sys.stdin.readline
#
# N, K = map(int, f_input().split())
#
# data = [tuple(map(int, f_input().split())) for _ in range(N)]
# data.sort(key=lambda d: (d[0], -d[1]))
# dp_w = [0] * N
# dp_v = [0] * N
# if data[0][0] <= K:
#     dp_w[0] = data[0][0]
#     dp_v[0] = data[0][1]
#
# for i in range(1, N):
#     if dp_w[i-1] + data[i][0] > K:
#         if dp_v[i-1] > data[i][1]:
#             dp_w[i] = dp_w[i - 1]
#             dp_v[i] = dp_v[i - 1]
#         else:
#             dp_w[i] = data[i][0]
#             dp_v[i] = data[i][1]
#     else:
#         dp_w[i] = dp_w[i - 1] + data[i][0]
#         dp_v[i] = dp_v[i - 1] + data[i][1]
#
# print(dp_v[-1])


# from itertools import combinations as comb
# N, K = map(int, input().split())
# things = list()
# for _ in range(N):
#     W, V = map(int, input().split())
#     things.append((W, V))
#
# max_val = 0
# # 무게의 합이 K를 초과하지 않는 물건의 조합들 가운데 V의 합이 가장 큰 경우
# for i in range(1, N + 1):
#     for c in comb(things, i):
#         if sum(t[0] for t in c) <= K:
#             if max_val < sum(t[1] for t in c):
#                 max_val = sum(t[1] for t in c)
#
# print(max_val)