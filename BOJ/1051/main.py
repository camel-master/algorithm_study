import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list()
for i in range(n):
    data.append(sys.stdin.readline().rstrip())


def get_max_area_of_square(n, m, data):
    area = 1
    for length in range(min(n, m), 1, -1):
        for k in range(0, n - length + 1):
            if area == length * length:
                break
            for l in range(0, m - length + 1):
                right_end = l + length - 1
                bottom_end = k + length - 1
                if data[k][l] == data[k][right_end] == data[bottom_end][l] == data[bottom_end][right_end]:
                    if area < length * length:
                        area = length * length
    return area


print(get_max_area_of_square(n, m, data))
