"""
BOJ 1978 소수 찾기

네이브하게 풀기
주어진 숫자들을 하나씩 소수인지 확인하는 알고리즘을 실행한다.
n = 숫자의 개수
m = 숫자의 크기
O(n * m)
"""
N = int(input())
numbers = map(int, input().split())
res = 0
for num in numbers:
    if num > 1:
        is_prime = True
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            res += 1
print(res)
