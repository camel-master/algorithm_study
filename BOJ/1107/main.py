"""
BOJ 1107 리모컨
https://www.acmicpc.net/problem/1107

0 <= channel number <= infinity

채널 N으로 이동하기 위한 최소 조작 회수를 구한다. (0 <= N <= 500,000)
초기 채널 번호는 100이다.
고장난 버튼 수 M의 범위는 0 <= M <= 10 이므로 모든 번호 버튼이 고장나거나 어떤 버튼도 고장나지 않을 수 있다.

입력이 다음과 같을 때
5457
3
6 7 8
5 4 5 5 + +
5 4 5 9 - -

고장나지 않은 버튼을 이용하여 이동하고자 하는 채널과 가장 가까운 채널을 입력한다. 가장 가까운 채널은 두개가 있을 수 있다.
+, - 버튼을 사용하여 원하는 채널로 이동한다.

또다른 입력 예시를 확인하면
500000
8
0 2 3 4 6 7 8 9
이동하고자 하는 채널의 가장 높은 자리수인 10만자리가 5이므로 누를 수 있는 수 중에 5와 가장 가까운 수를 선택한다.
여기서는 1, 5를 누를 수 있으므로 5를 선택한다.
5
1만자리의 수를 선택하기 위해 1만자리 수 0과 가까운 누를 수 있는 번호를 선택한다. 0은 5보다 1이 더 가까으므로
1을 선택한다.
5 1
1천 자리의 수를 선택하기 위하 1천 자리 수 0과 가까운 누를 수 있는 번호를 선택한다. 0은 5보다 1이 더 가까으므로
5 1 1
1백 자리의 수를 선택하기 위하 1백 자리 수 0과 가까운 누를 수 있는 번호를 선택한다. 0은 5보다 1이 더 가까으므로
5 1 1 1
1십 자리의 수를 선택하기 위하 1십 자리 수 0과 가까운 누를 수 있는 번호를 선택한다. 0은 5보다 1이 더 가까으므로
5 1 1 1 1
1의 자리의 수를 선택하기 위하 1의 자리 수 0과 가까운 누를 수 있는 번호를 선택한다. 0은 5보다 1이 더 가까으므로
5 1 1 1 1 1
원하는 채널과 가장 가까운 수를 만들었고 이를 NC라 하자
abs(NC - N) = 111111
가장 가까운 채널로 이동하기 위한 숫자버튼 조작 6번 + 한 채널씩 이동한 조작 111111번 하여 총 111117번의 조작이 필요하다.

다른 입력예시를 확인하자.
80000
2
8 9
누를 수 있는 숫자 버튼은 {1, 2, 3, 4, 5, 6, 7, 0}이다.
8과 가장 가까운 수는 7이므로
7
이전 자리 수가 누르고자 하는 수보다 작으므로 누를 수 있는 가장 큰 수를 누른다.
71111

입력할 수 있는 숫자 버튼을 확인한다.
이동해야할 채널이 초기 채널과 같으면 조작 횟수 0을 출력한다.
for idx in range(len(숫자문자열)):
    각 자리 수 = 숫자문자열[idx]
    if 각 자리 수 in pressable_button:
        NC += 각 자리 수
        res += 1    # count button pressing
    else:
        if 숫자문자열[idx-1] == NC[idx-1]:
            최소차 = 9 로 초기화
            for 버튼숫자 in pressable_button:
                if 각자리 수 - 버튼숫자 < 최소차:
                    최소차 = Abs(각자리 수 - 버튼숫자)
                    최소차 숫자 = 버튼숫자
            NC += 최소차 숫자
            res += 1
        elif: 숫자문자열[idx-1] > NC[idx-1]:
            NC += max(pressable_button)
            res += 1
        else:
            NC += min(pressable_button)
            res += 1
res += abs(NC - N)
print(res)

위 알고리즘의 시간복잡도를 계산해보면 N의 길이만큼 돌면서 가장 가까운 수를 눌러야 하므로 O(len(N) * (10 - M))이 된다.
N은 5만까지이므로 최대 6자리 까지다. 또한 누를 수 있는 숫자버튼의 최대 개수는 10개이다.
따라서 최대 연산 회수는 6 * 10 = 60 이다. 시간제한은 2초이므로 위의 알고리즘은 사용할 수 있는 알고리즘이다.

생각했던 알고리즘으로 채널 99를 맞춘다고 했을 때 숫자 9 버튼을 이용할 수 있다고 치면
9 9 와 같이 9를 두번 누르게 되어 틀린 결과를 도출하게 된다.
99이면 초기 채널 번호 100에서 - 버튼을 한 번만 누르면 되기 때문이다.

1000
누를 수 있는 키는 1, 9밖에 없다고 할 때,
1111로 만든 뒤 -버튼을 111회 = 112회 버튼 누름
999로 만든 뒤 +버튼을 1회 = 4회 버튼 누름.
누를 수 있는 버튼을 사용한 모든 곱집합을 구한다.
절대값(N - 각 곱집합 원소 들) 중 가장 작은 값 + 곱집합 원소의 길이 = 원하는 해
채널 최대 6자리 이므로,
10 * 10 * 10 * 10 * 10 * 10 = 1,000,000 개의 곱연산 결과가 나오게 된다.
따라서 1,000,000개의 원소 가운데 N과의 차가 가장 적은 것을 선택하는 것이므로
이 알고리즘을 사용하면 O(10^len(N))으로 해를 찾을 수 있다. 따라서 제한 시간 2초 내에 문제를 풀 수
있을것으로 판단된다.

-------------------------------------------------------------------------------------
눈여겨 볼만한 코드
class Remocon:
    def __init__(self):
        self.buttons = list(range(10))

    def distroy(self, b):
        self.buttons.remove(b)

    def __getitem__(self, n):
        l = len(self.buttons)
        result, digit = 0, 1
        while n >= l:
            result += self.buttons[n%l] * digit
            n //= l
            if self.buttons[0]:
                n -= 1
            digit *= 10
        result += self.buttons[n%l] * digit
        return result

    def least_button_push(self, target):
        if not self.buttons:
            result = float('inf')
        elif self.buttons == [0,]:
            result = target + 1
        elif self[0] > target:
            result = self[0] - target + 1
        else:
            lo, hi = 0, 10
            while self[hi] <= target:
                hi *= 10
            while hi - lo > 1:
                m = (lo + hi) // 2
                if self[m] < target:
                    lo = m
                else:
                    hi = m
            lower, higher = self[lo], self[hi]
            result = min(len(str(lower)) + abs(lower - target),
                        len(str(higher)) + abs(higher - target))
        return min(result, abs(target - 100))


remocon = Remocon()
target = int(input())
if int(input()):
    for button in map(int, input().split()):
        remocon.distroy(button)
print(remocon.least_button_push(target))
"""
from itertools import product
import sys
f_input = sys.stdin.readline

N = int(f_input().rstrip())
M = int(f_input().rstrip())
pressable_btn = {str(i) for i in range(10)}
if M > 0:
    for broken_btn in map(str, f_input().rstrip().split()):
        pressable_btn.remove(broken_btn)
if N == 100:
    print(0)
else:
    min_diff = 1_000_000
    len_n_str = 0
    c_diff = 0
    for i in range(1, 7):
        for cand_ch in product(pressable_btn, repeat=i):
            n_str = ''.join(cand_ch)
            c_diff = abs(N - int(n_str))
            if c_diff < min_diff:
                min_diff = c_diff
                len_n_str = len(n_str)

    if abs(100 - N) < min_diff + len_n_str:
        print(abs(100 - N))
    else:
        print(min_diff + len_n_str)
