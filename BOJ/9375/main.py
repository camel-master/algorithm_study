"""
BOJ 9375 패션왕 신해빈
https://www.acmicpc.net/problem/9375

경우의 수 문제
입력 데이터가 다음과 같은 경우
hat headgear
sunglasses eyewear
turban headgear
{headgear: 2, sunglasses: 1}
각 의상 종류별로 걸치지 않는 경우의 수가 있으므로
{headgear: 2 + 1, sunglasses: 1 + 1}
따라서 총 경우의 수는 3 * 2 = 6 이다.
하지만 아무것도 입지 않은 경우는 제외 해야 하므로 6 -1 = 5 가 답이 된다.

Counter를 사용하여 item 별 수량을 파악하도록 한다.
"""
from collections import Counter
import sys

f_input = sys.stdin.readline

test_case = int(f_input())
for _ in range(test_case):
    n = int(f_input())
    wears = [f_input().split()[1] for _ in range(n)]
    res = 1
    for wear_cnt in Counter(wears).values():
        res *= (wear_cnt + 1)
    print(res - 1)
