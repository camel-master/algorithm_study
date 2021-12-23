import sys
n, k = map(int, sys.stdin.readline().rstrip().split())


def get_kth_deleted_primenumber(n, k):
    num_list = list()
    for i in range(2, n + 1):
        num_list.append(i)
    count = 0
    while len(num_list) > 0:
        prime_number = num_list[0]
        for e in num_list:
            if e % prime_number == 0:
                num_list.remove(e)
                count += 1
                if count == k:
                    return e


print(get_kth_deleted_primenumber(n, k))
