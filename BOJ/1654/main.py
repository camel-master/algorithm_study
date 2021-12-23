"""
BOJ 1654 랜선 자르기
https://www.acmicpc.net/problem/1654

K개의 랜선을 사용하여 N개 이상의 랜선을 만든다.
최대로 만들 수 있는 길이의 총 합은?

1 <= K <= 10,000
1 <= N <= 1,000,000

1 <= 랜선의 길이 <= 2^31 - 1

test cases
4 4
100
100
100
100

4 4
480
120
120
120
"""
K, N = map(int, input().split())    # K <= N
cable_lengths = list()
for _ in range(K):
    cable_lengths.append(int(input()))

s = 1
e = max(cable_lengths)
# e = 2 ** 31 - 1   --> binary search의 max 범위를 최대한 작게 설정하도록 연습한다.

while s <= e:
    m = (s + e) // 2
    cable_cnt = 0
    for cable_len in cable_lengths:
        cable_cnt += cable_len // m
    """
    f(x)는 x일 때의 값이라 하고 N을 찾고자 하는 값이라고 했을 때
    f(x) == N 이면 원하는 값을 찾은 것으로 반복문을 종료하고
    찾지 못하면 탐색할 범위를 반으로 좁혀서 N을 만족할 x가 들어있는 절반을
    선택하여 반복문을 계속 실행한다.
    따라서 다음과 같은 형태의 조건문을 보인다.
    m = (e-s) // 2 + s
    if f(m) > N:
        e = m - 1
    elif f(m) < N:
        s = m + 1
    else:
        return m
        
    이 문제와 max 값을 묻는 문제의 경우는 구조가 달라진다.
    max 값을 찾을 때까지 계속 binary search를 진행할 필요가 있다.
    따라서 다음가 같은 조건문 형태를 보인다.
    m = (e-s) // 2 + s
    if f(m) >= N:
        s = m + 1
    else:
        e = m - 1
    
    min 값을 찾는 binary search 코드는 어떨까?
    m = (e-s) // 2 + s
    if f(m) <= N:
        e = m - 1
    else:
        s = m + 1
    과 같은 형태의 코드가 작성될 것이다.
    """
    if cable_cnt >= N:
        s = m + 1
    else:
        e = m - 1

print(e)
