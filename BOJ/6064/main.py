"""
BOJ 6064 카잉달력
https://www.acmicpc.net/problem/6064

M = 10 이고 N = 12 일 때 <M:N> 까지 데이터의 변화를 살펴본다.
{
    1: <1:1>, 2: <2:2>, 3: <3:3>, 4: <4:4>, 5: <5:5>, 6: <6:6>, 7: <7:7>, 8: <8:8>, 9: <9:9>, 10: <10:10>,
    11: <1:11>, 12: <2:12>, 13: <3:1>, 14: <4:2>, 15: <5:3>, 16: <6,4>, 17: <7:3>, 18: <8:4>, 19: <9:5>, 20: <10:6>
    ...
    51: <1:3>, 52: <2:4>, 53: <3:5>, 54: <4:6>, 55: <5:7>, 56: <6:8>, 57: <7:9>, 58: <8:10>, 59: <9:11>, 60: <10:12>
}

1 ~ M 까지의 숫자와 1 ~ N 까지의 숫자를 순차적으로 접근 해가면서 순서쌍을 만들어 나가다가 순서쌍이 (M, N)이 되면 종료되도록 한다.
순서쌍을 만들 때 마다 year를 + 1한다. 순서쌍이 (x, y)에 다다르면 year를 출력하고 종료 될 때까지 (x, y)를 찾지 못하면 -1을 출력한다.

시간복잡도
이런 경우 시간복잡도를 어떻게 계산하는지 모르겠다.

공간복잡도
N + M 개의 정수를 저장할 공간이 필요하다. 따라서 메모리 제한은 통과할 수 있다.


1
10 12 3 9

1
10 12 7 2

위의 알고리즘으로는 시간초과가 난다. 시간복잡도는 어떻게 계산하지???
x가 되려면 y도 x - 1 만큼 변경되어야 한다.
if x가 N을 초과 then y의 초기값 = N_list[x-N-1]
else y의 초기 값 =  N_list[x-1]
이제 N_list의 현재 index를 M씩 증가시켜 가면서 y와 일치하는 값이 나오는지 확인.
year = x 로 경과 년수를 초기화
이후 N년 씩 더해간다.

1
10 12 3 9

3: <3:3>
13: <3:(3 + 10)%12> = <3:1>
23: <3:11>
33: <3:(11 + 10)%12> = <3:9>
...
최대 40000 까지만 돌도록 제한

1
10 10 10 10
->10

1
13 11 5 6
->83
5 <5:5>
18 <5:5+13> -> <5:18> -> <5:7>
31 <5:8+13> -> <5:21> -> <5:10>
44 <5:10+13> -> <5:23> -> <5:1>
57 <5:1+13> -> <5:14> -> <5:3>
70 <5:3+13> -> <5:16> -> <5:5>
83 <5:5+13> -> <5:18> -> <5:7>

1
10 12 2 12
2   <2:2>
12  <2:12>
22  <2:22> -> <2:10>
32  <2:20> -> <2:8>
42  <2:18> -> <2:6>
52  <2:16> -> <2:4>
52  <2:14> -> <2:2>
52  <2:12>

1
10 4 5 4
5   <5:1>
15  <5:11> -> <5:3>
25  <5:13> -> <5:1>

일단 반례 목록을 드립니다. 원래 이런 건 스스로 찾는 것이 가장 좋습니다. 정말로, 질문 게시판을 보면 아무거나 넣었더니 반례가 금방 나오는 질문이 굉장히 많습니다.

Q: (1씩 더해가면서 확인하는 코드) 왜 시간초과인가요?

A: 답이 나와도 너무 오래 걸리면 안 됩니다. 여기에 있는 맨 처음 케이스에서 x와 y를 1씩 더하는 것만 세도 32억 번의 연산이 필요합니다. 힌트를 드리자면 일단 <x, y> 말고 x만 알맞은 값이 나오려면 몇 번째 해가 되어야 하는지 생각해 보세요.

Q: 예제는 / 비쥬얼 스튜디오에서는 / 이클립스에서는 / 파이참에서는 / 등등 잘 나오는데 ...

A: 예제 입출력은 "예를 들어 이런 입력을 줄 것이고 이 때는 이렇게 출력해야 한다"라는 뜻이지, "이게 잘 돌아가면 대충 맞는 코드일 것이다"라는 뜻이 절대 아닙니다. https://www.acmicpc.net/blog/v...

Q: 코드가 너무 복잡해진 것 같습니다.

A: 아래 데이터 중 특수 케이스라고 부를 만한 건 없습니다. 단순히 이 데이터들을 맞기 위해 코드를 수정하지 말고, 논리에 근본적으로 무슨 오류가 있는지를 생각하세요.

Q: 문제 설명에서 11번째 해는 1:11이고 13번째 해는 3:1이라고 했는데 이거 잘못된 거 아닌가요?

A: 네, 잘못된 거 아닙니다.

15
40000 39999 39999 39998
40000 39999 40000 39999
40000 40000 40000 39999
40000 39998 40000 39997
39999 2 39998 2
3 40000 3 39999
40000 3 40000 3
8 2 4 2
10 12 2 12
12 10 12 10
12 10 1 1
12 6 12 6
10 1 5 1
1 10 1 5
1 1 1 1

답:
1599959999
1599960000
-1
-1
39998
39999
120000
4
12
60
1
12
5
5
1

[sudo code]
if x > N then
    year = (x, x-N)
else
    year = (x, x)
f_year = year
while True {
    year[1] = (year[1] + M) % N
    if year[1] == 0 then
        year[1] = N
    if year == (x, y) then
        print x
        break
    if year == f_year then
        print -1
        break

[참고할 코드]
import sys


def sol():
    read = sys.stdin.readline
    for _ in range(int(read())):
        M, N, x, y = [int(x) for x in read().split()]
        print(eea(M, N, x, y))


def e_gcd(x, y):
    s = [1, 0]
    t = [0, 1]
    r = [x, y]
    while r[-1] != 0:
        q = r[-2] // r[-1]
        r = [r[-1], r[-2] - q * r[-1]]
        s = [s[-1], s[-2] - q * s[-1]]
        t = [t[-1], t[-2] - q * t[-1]]
    return [r[0], s[0], t[0]]


def eea(M, N, x, y):
    gcd, s, t = e_gcd(M, N)
    if x % gcd != y % gcd:
        return -1
    else:
        return (x - M * s * (x - y) // gcd) % (M * N // gcd)


if __name__ == "__main__":
    sol()
"""
import sys
f_input = sys.stdin.readline
T = int(f_input().rstrip())
for _ in range(T):
    M, N, x, y = map(int, f_input().rstrip().split())
    year_cnt = x
    # x 또는 y로 나눠 떨어졌을 때가 x 또는 y 자체가 되어야 한다.
    # 그런데 여기서는 단순히 몇년이 지나는지를 주기적으로 카운팅만 하면되니 x, y의 초기값에 각각 -1을 하여
    # 기존 1 ~ x, 1 ~ y까지의 범위를 0 ~ x-1, 0 ~ y-1까지를 범위로 변경한다.
    x -= 1
    y -= 1
    year = [x, x % N]
    f_year = year[:]
    if year[0] == x and year[1] == y:
        print(year_cnt)
    else:
        while True:
            year[1] = (year[1] + M) % N
            year_cnt += M
            if year[0] == x and year[1] == y:
                print(year_cnt)
                break
            if year[0] == f_year[0] and year[1] == f_year[1]:
                print(-1)
                break
# import sys
#
# f_input = sys.stdin.readline
#
# T = int(f_input().rstrip())
# for _ in range(T):
#     M, N, x, y = map(int, f_input().rstrip().split())
#     # if x > N:
#     #     year = [x, x - N]
#     # else:
#     #     year = [x, x]
#     year = [x, x % N]
#     f_year = year[:]
#     year_cnt = x
#     if year[0] == x and year[1] == y:
#         print(x)
#     else:
#         while True:
#             year[1] = (year[1] + M) % N
#             year_cnt += M
#             if year[1] == 0:
#                 year[1] = N
#             if year[0] == x and year[1] == y:
#                 print(year_cnt)
#                 break
#             if year[0] == f_year[0] and year[1] == f_year[1]:
#                 print(-1)
#                 break


    # M, N, x, y = map(int, f_input().rstrip().split())
    # year = x
    # if x > N:
    #     ny = x - N
    # else:
    #     ny = x
    # is_found = False
    # while year <= 40_000:
    #     if ny == y:
    #         is_found = True
    #         break
    #
    #     year += M
    #     # print(year, ny + M)
    #     if (ny + M) % N == 0 or (ny + M) % N == y:
    #         is_found = True
    #         break
    #     else:
    #         ny = (ny + M) % N
    #
    # if is_found:
    #     print(year)
    # else:
    #     print(-1)

    # M, N, x, y = map(int, f_input().rstrip().split())
    # M_idx = 0
    # N_idx = 0
    # M_list = [n for n in range(1, M + 1)]
    # N_list = [n for n in range(1, N + 1)]
    # year = 0
    # is_found = False
    # while M_list[M_idx] != M or N_list[N_idx] != N:
    #     year += 1
    #     if M_list[M_idx] == x and N_list[N_idx] == y:
    #         is_found = True
    #         break
    #     if M_idx == len(M_list) - 1:
    #         M_idx = 0
    #     else:
    #         M_idx += 1
    #     if N_idx == len(N_list) - 1:
    #         N_idx = 0
    #     else:
    #         N_idx += 1
    #
    # if is_found:
    #     print(year)
    # else:
    #     print(-1)
