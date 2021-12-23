"""
BOJ 2609 최대공약수와 최소공배수

시간제한 1초로 약 1억번의 연산이 가능한 시간.
최대공약수와 최소공배수를 구해야 하는 숫자의 크기는 가각 10,000 이하이므로
O(n^2)으로 풀어도 제출 가능.

유클리드 호제법으로 최대공약수를 구한다.


(A // GCD) * (B // GCD) * GCD = LCM

"""


# def get_gcd(A, B):
#     max_n = int()
#     min_n = int()
#     if A - B >= 0:
#         max_n = A
#         min_n = B
#     else:
#         max_n = B
#         min_n = A
#     remainder = max_n % min_n
#     if remainder == 0:
#         return min_n
#     else:
#         return get_gcd(min_n, remainder)
def get_gcd(A, B):
    if B != 0:
        return get_gcd(B, A % B)
    else:
        return A

A, B = map(int, input().split())

GCD = get_gcd(A, B)
LCM = (A // GCD) * (B // GCD) * GCD
print(GCD)
print(LCM)
