"""
Programmers k진수에서 소수 개수 구하기
https://programmers.co.kr/learn/courses/30/lessons/92335

주어진 수를 k진수로 변환한 문자열을 '0'을 기준으로 나눠 각 요소별로 소수인지 확인한다.
3 <= k <= 10
k진수로 만드는데 필요한 시간복잡도는 O(log n)
각 수별로 소수인지 판별하는 시간복잡도는 O(n)
1,000,000에 대해 k진법으로 변환했을 때 그 숫자열의 길이가 가장 긴 경우는 3진수가 될 때일 것이다.
1,000,000을 3진수로 표현하면 212,210,202,001 총 12자리 수이다.
12자리 중 0이 아닌 수가 가장 길게 연속되게 나오는 경우를 L이라 하면
O(L)만큼의 시간복잡도이다.
"""
def get_prime_yn(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def get_num_list(base, k):
    num_list = list()
    temp = list()
    while base >= k:
        temp.append(base % k)
        base //= k
        if base < k:
            temp.append(base)
    num = ''
    for ch in temp[-1::-1]:
        if ch == 0:
            if num != '':
                num_list.append(int(num))
                num = ''
        else:
            num += str(ch)
    if num != '':
        num_list.append(int(num))

    return num_list


def solution(n, k):
    prime_cnt = 0
    for n in get_num_list(n, k):
        if get_prime_yn(n):
            prime_cnt += 1

    return prime_cnt

n = 437674
k = 3
print(solution(n, k))
