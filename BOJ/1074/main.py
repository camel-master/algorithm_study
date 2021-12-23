"""
BOJ 1704 Z

한 변이 2^N 길이인 평면을 만든다.
2^N 길이이므로 정확하게 4등분이 가능하다. 평면을 4개로 나눠 사분면으로 만든다.
이 때 각 사분면의 첫번째 요소를 특정지을 수 있다.
    N > 1을 만족하는 동안 다음의 과정을 반복한다.
    1. 현재 사분면을 이루는 총 원소 수를 4로 나눈 숫자를 가중치 W라 하자.
    2. 2 ~ 4사분면의 번호를 각각 2, 3, 4라 하면 각 사분면의 첫번쨰 원소의
       값은 (사분면 번호) * W가 된다.
    3. N = N - 1
N == 1 일 때, 시작 위치로 부터 오른쪽, 아래쪽, 오른쪽대각에 위치한 요소들의 값을
시작위치로 부터 1씩 증가시켜가며 업데이트 한다.

평면 정보 중 (r, c)에 해당하는 값을 찾아 반환한다.

위의 solution은 메모리 초과를 보였다. 메모리 초과가 발생한 이유는
N의 최댓값이 15로 2^15 = 32768 이므로 평면을 이루는 칸의 최대 개수는
2^15 x 2^15 = 1,073,741,824 개가 된다.
정수형을 4byte라 할 때 총 1,073,741,824 개의 공간이 필요하므로
1,073,741,824 x 4 = 4GB의 메모리를 필요로 하게 된다. 문제의 제한 조건에
메모리 제한이 512MB이므로 메모리 초과 결과를 보이게 된다.

테이블을 생성하여 업데이트 시키는 대신 4분면을 좁혀가면서 해당 사분면의 첫째 값만 기억하고
(r, c) 요소에 도착하면 해당 값을 반환하도록 하면 메모리 제한을 통과할 수 있을 것으로 생각된다.
또한 하나의 평면을 4개로 나눌 때 모든 사분면을 다 확인하는 것이 아니라 (r, c)를 포함한
사분면만 확인해 나갈 수 있도록 가지치기를 하여 좀 더 효율적인 탐색이 가능하도록 수정할 수 있을것 같다.
"""
# N, r, c = map(int, input().split())
# map_info = [[0] * 2 ** N for _ in range(2 ** N)]
#
#
# def visit(map_info, N, sr, sc):
#     if N == 1:
#         # 좌, 하, 우대각 항목에 대해 시작 점에 각각 1, 2, 3을 더한 수로 채운다.
#         map_info[sr][sc+1] = map_info[sr][sc] + 1
#         map_info[sr+1][sc] = map_info[sr][sc] + 2
#         map_info[sr+1][sc+1] = map_info[sr][sc] + 3
#     else:
#         map_size = 2 ** N
#         w = map_size ** 2 // 4
#         for m in range(4):
#             if m == 0:
#                 visit(map_info, N - 1, sr, sc)
#             elif m == 1:
#                 # (sr, sc + map_size // 2)에 w * m 추가
#                 map_info[sr][sc + map_size // 2] = map_info[sr][sc] + w * m
#                 visit(map_info, N - 1, sr, sc + map_size // 2)
#             elif m == 2:
#                 map_info[sr + map_size // 2][sc] = map_info[sr][sc] + w * m
#                 visit(map_info, N - 1, sr + map_size // 2, sc)
#             else:
#                 map_info[sr + map_size // 2][sc + map_size // 2] = map_info[sr][sc] + w * m
#                 visit(map_info, N - 1, sr + map_size // 2, sc + map_size // 2)
#
#
# visit(map_info, N, 0, 0)
# print(map_info[r][c])


N, r, c = map(int, input().split())


def visit(N, sr, sc, fv):
    if N == 1:
        # 좌, 하, 우대각 항목에 대해 시작 점에 각각 1, 2, 3을 더한 수로 채운다.
        # map_info[sr][sc+1] = map_info[sr][sc] + 1
        # map_info[sr+1][sc] = map_info[sr][sc] + 2
        # map_info[sr+1][sc+1] = map_info[sr][sc] + 3
        rw = r - sr
        cw = c - sc
        if rw == 0 and cw == 0:
            return fv
        elif rw == 0 and cw == 1:
            return fv + 1
        elif rw == 1 and cw == 0:
            return fv + 2
        else:
            return fv + 3
    else:
        map_size = 2 ** N
        w = map_size ** 2 // 4
        br = sr + map_size // 2
        bc = sc + map_size // 2
        # # # #
        # # # #
        # # * #
        # # # #
        if r < br and c < bc:
            # 1사분면
            return visit(N - 1, sr, sc, fv)
        elif r < br and c >= bc:
            # 2사분면
            return visit(N - 1, sr, sc + map_size // 2, fv + w)
        elif r >= br and c < bc:
            # 3사분면
            return visit(N - 1, sr + map_size // 2, sc, fv + 2 * w)
        else:
            # 4사분면
            return visit(N - 1, sr + map_size // 2, sc + map_size // 2, fv + 3 * w)


print(visit(N, 0, 0, 0))
