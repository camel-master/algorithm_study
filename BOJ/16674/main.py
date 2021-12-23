import sys
N = sys.stdin.readline().rstrip()
def get_number_type(N):
    year = '2018'
    number_type = int()
    for elem_of_N in N:
        if elem_of_N not in year:
            return 0
    for e in year:
        if N.count(e) == 0:
            return 1
        if e == '8' and N.count(e) > 0:
            cnt_list = [0] * len(year)
            for i in range(0, len(year)):
                cnt_list[i] = N.count(year[i])
            if cnt_list[0] == cnt_list[1] == cnt_list[2] == cnt_list[3]:
                return 8
            else:
                return 2

print(get_number_type(N))