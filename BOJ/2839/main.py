"""
BOJ 2839 설탕배달
https://www.acmicpc.net/problem/2839
설탕포장은 3kg, 5kg이 있다.
N kg을 배달하기 위해 가져가야 할 봉지 가장 적은 수를 구하기

1의 자리 수를 0으로 대체하면 5의 배수가 되나?
11 => 10
9999 = > 9990
된다!

그런데 N 자체가 3의 배수인지 확인하는 절차도 필요할 거 같다.
12의 경우 10 + 2로 만들면 2 % 3 != 0 이지만
12 % 3 이면 3kg 용량 4봉지로 배달할 수 있기 때문이다.

그렇다면 N이 5의 배수인지 확인하고 아니라면 N에서 3씩 빼가도록 하자.
3을 뺄때마다 봉지를 하나씩 추가한다.
    3을 뺀 수가 5의 배수가 된다면 나눈 몫 만큼 봉지를 더한다.

"""
import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
while N > 0:
    if N % 5 == 0:
        cnt += N // 5
        N = 0
    else:
        N -= 3
        cnt += 1

if N == 0:
    print(cnt)
else:
    print(-1)
