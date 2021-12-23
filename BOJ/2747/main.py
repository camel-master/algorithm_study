import sys
n = int(sys.stdin.readline().rstrip())


def get_fibonacci_number(n):
    number_list = [0, 1]
    if n == 1:
        return number_list[0]
    if n == 2:
        return number_list[1]
    for i in range(2, n + 1):
        number_list.append(number_list[i - 1] + number_list[i - 2])
    return number_list[n]


print(get_fibonacci_number(n))
