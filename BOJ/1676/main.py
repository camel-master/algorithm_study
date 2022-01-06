"""
BOJ 1676 팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676

팩토리얼 함수를 사용하여 N 팩토리얼을 구한다.
N factorial을 문자열로 변환하고 이를 f_str이라 하자.
f_str의 마지막 문자부터 선형탐색하면서 '0'이 아닌 문자를 만날 때까지 '0'의 개수를 카운팅한다.

시간복잡도 확인
factorial() 의 시간복잡도는 O(N),
0의 개수를 뒤에서 부터 찾는 경우 O(len(str(factorial(N)))의 복잡도가 된다.
N < len(str(factorial(N)) 이고 N = 500 일 때 len(str(factorial(N)) = 1135이다.
따라서 시간 제한 2초를 통과할 수 있으므로 사용할 수 있는 알고리즘이다.

공간복잡도 확인
가장 큰 N에 대해 1135개의 문자를 저장해야 하며 파이썬에서 문자열의 1개 문자는 1byte 크기를
가지므로 1135byte = 1.1kb로 메모리 제한 128mb보다 낮기 때문에 사용할 수 있는 알고리즘이다.

참고할만한 코드
# 5의 배수 마다 0이 한 개씩 추가된다.
# 25 = 5 * 5 이므로 25의 배수 마다 0이 한 개씩 추가된다.
# 125 = 5 * 5 * 5 이므로 125의 배수 마다 0이 한 개씩 추가된다.
a=int(input())
print(a//5+a//25+a//125)

"""
from math import factorial
import sys
input = sys.stdin.readline

N = int(input().rstrip())
f_str = str(factorial(N))
zero_cnt = 0
for ch in f_str[::-1]:
    if ch == '0':
        zero_cnt += 1
    else:
        break

print(zero_cnt)
