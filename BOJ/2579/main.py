"""
BOJ 2579 계단 오르기
https://www.acmicpc.net/problem/2579

계단 오르기 규칙
1. 한 번에 1칸 또는 2칸만 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟으면 안된다. 즉 첫번째, 두번째, 세번째 칸을 모두 밟아선 안된다.
   (시작 위치는 계단이 아니다.)
3. 마지막 계단은 반드시 밟아야 한다.

계단마다 점수가 주어지며 해당 칸에 오를 때 그 점수를 총점에 합산한다.
이때 최대로 받을 수 있는 총점은?

계단의 수 S는 1 <= S <= 300 이다.

전형적인 DP 문제이다. 완탐으로 푸는 경우 현재 위치에서 다음 계단으로 오를 수 있는 경우의 수가 두 가지이므로
O(2^n)의 시간복잡도가 되며 시간제한 1초 내에 풀 수가 없다.

입력의 예가 다음과 같다고 해보자
6
10
20
15
25
10
20

위의 계단 정보를 담고 있는 배열을 ST라고 했을 때
각 계단별로 해당 계단까지 올랐을 때의 최대 값을 가지는 DP테이블을 하나 선언한다.
총 6개의 계단이므로 오르지 않았을 경우를 더해 7개의 데이터를 생성한다. 또한
첫번째 계단까지 올랐을 때 최대 값은 ST[1]로 고정이다. 따라서 초기화된 DP테이블은
다음과 같다.
DP = [0, 10, 0, 0, 0, 0, 0]

두 번쨰 칸 부터 해당 칸까지의 최대 점수를 구하기 위해서는 현재 계단을 i번째 계단이라 했을 때
(i - 1)번째 계단에서 +1한 경우와 (i - 2)번째 계단에서 +2한 경우를 생각해볼 수 있다.
따라서 점화식은 다음과 같이 작성할 수 있다.
DP[i] = max((ST[i] + DP[i-1] - DP[i-2]), (ST[i] + DP[i-2])

위의 점화식은 잘못된 점화식이다.

Test case 1
5
30
30
30
30
30

expected: 120

Test case 2
6
10
20
15
25
10
20

expected: 75

참고할 코드
import sys

N = int(sys.stdin.readline())
stair = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

d1 = [0] * 301
d2 = [0] * 301

for i in range(1, N+1):
    d1[i] = d2[i-1] + stair[i]
    d2[i] = max(d1[i-2], d2[i-2]) + stair[i]

print(max(d1[N], d2[N]))
"""
import sys

f_input = sys.stdin.readline

N = int(f_input())
st = [0] + [int(f_input()) for _ in range(N)]
if N == 1:
    print(st[N])
elif N == 2:
    print(st[N - 1] + st[N])
else:
    DP = [[0] * (N + 1) for _ in range(2)]
    DP[0][1] = st[1]
    DP[1][2] = st[2]
    DP[0][2] = DP[0][1] + st[2]
    for i in range(3, N + 1):
        DP[0][i] = DP[1][i - 1] + st[i]
        DP[1][i] = max(DP[0][i - 2], DP[1][i - 2]) + st[i]

    print(max(DP[0][-1], DP[1][-1]))
