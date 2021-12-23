"""
Fly me to the Alpha Centauri

10 까지 이동한다고 해보자.
0부터 시작하여 0+1까지 이동
1부터 시작하여 1+2까지 이동
3부터 시작하여 3+3까지 이동
6부터 시작하여 10까지 이동 (안됨)
6부터 시작하여 6+2까지 이동
8부터 시작하여 8+1까지 이동
9부터 시작하여 9+1까지 이동

16까지 이동
0부터 시작하여 0+1까지 이동
1부터 시작하여 1+2까지 이동
3부터 시작하여 3+3까지 이동
6부터 시작하여 6+4까지 이동
10부터 시작하여 10+3까지 이동
13부터 시작하여 13+2까지 이동
15부터 시작하여 15+1까지 이동

int((도착위치 - 시작위치) ** 0.5)만큼 1씩 증가 후 1씩 감소 시킨다.

도착위치 - 현재위치  < 현재 순간이동 거리.
"""

T = int(input())
test_case = list()
for _ in range(T):
    test_case.append(list(map(int, input().split())))

for c_pos, a_pos in test_case:
    dist = 0
    warp_time = 0
    while True:
        if c_pos == a_pos:
            break
        if a_pos - c_pos > dist:
            dist += 1
            c_pos += dist
        else:
            dist -= 1
            if dist < 1:
                dist = 1
            c_pos += dist
        warp_time += 1
    print(warp_time)
# for s_pos, e_pos in test_case:
#     c_pos = s_pos
#     speed = 0
#     using_cnt = 0
#
#     for _ in range(int((e_pos - s_pos) ** 0.5)):
#         speed += 1
#         c_pos += speed
#         using_cnt += 1
#     while True:
#         if speed < 1:
#             speed = 1
#         else:
#             speed -= 1
#         c_pos += speed
#         using_cnt += 1
#         if c_pos == e_pos - 1:
#             break
#
#     print(using_cnt)
