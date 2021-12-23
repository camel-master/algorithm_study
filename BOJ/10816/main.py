"""
BOJ 10816 숫자 카드 2
https://www.acmicpc.net/problem/10816

숫자 카드 N개

찾을 정수 M개

hash를 사용하여 풀어본다.
등장하는 카드에 적힌 숫자를 key로 갖고 등장할 때마다 value를 1씩 더해간다.

key로 접근하여 각각의 요소가 몇번이나 등장했는지 확인한다.
key error 발생 시에는 0을 출력한다.

단순히 리스트 안에 각요소별로 몇개의 요소가 있는지 확인할 떄는  Counter를 사용하면 속도를 향상시킬 수 있다.
"""
from collections import defaultdict
import sys
f_input = sys.stdin.readline


N = int(f_input())
cards = defaultdict(int)
for c_num in map(int, f_input().rstrip().split()):
    cards[c_num] += 1
M = int(f_input())
for s_num in map(int, f_input().rstrip().split()):
    try:
        print(cards[s_num], end=' ')
    except KeyError:
        print(0)
