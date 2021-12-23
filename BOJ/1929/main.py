"""
BOJ 1929 소수 구하기
"""
M, N = map(int, input().split())
# 우선 N 이하의 소수를 구한다.
prime_nums = list()

# 1 ~ 1000 모든 수가 소수라고 가정
prime_numbers = [True for i in range(N + 1)]
prime_numbers[1] = False
for i in range(2, int(N ** 0.5) + 1):  # 2 ~ n의 제곱근 까지 확인한다.
    if prime_numbers[i]:
        j = 2
        while i * j <= N:
            prime_numbers[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(M, N + 1):
    if prime_numbers[i]:
        print(i)
