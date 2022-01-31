"""
BOJ 2042 구간 합 구하기
https://www.acmicpc.net/problem/2042

누적합을 사용한다고 생각해보자.
N개의 요소에 대해 누적합 테이블을 만들고 테이블의 값을 채우는데는 O(N)이 소요된다.
M번 데이터의 값이 변동되는데 변동 될 때마다 가장 앞의 데이터가 변동된다고 생각해보면
O(NM)의 시간복잡도가 되겠다. 누적합 테이블만 있으면 구간 데이터를 구하는데는 O(1)
이면 된다. 본 문제에서 O(NM)의 최대 연산 회수는 1,000,000 * 10,000 이므로
총 10,000,000,000 번으로 시간제한을 만족하기 어렵다.

세그먼트 트리를 사용하여 풀어보자.


결론:
    구간합을 구할 때 더해야할 값들이 자주 변동되는 경우는 세그먼트 트리를 사용하고
    더하는 값이 fixed인 경우는 누적합을 사용하는 것이 유리하다.

"""
import sys

f_input = sys.stdin.readline

N, M, K = map(int, f_input().rstrip().split())

nums = [int(f_input()) for _ in range(N)]

# initialization of segment tree
node_cnt = 0
i = 0
while 2 ** i <= len(nums):
    node_cnt += 2 ** i
    i += 1
node_cnt += 2 ** i
seg_tree = [0] * (node_cnt + 1)



for _ in range(M + K):
    a, b, c = map(int, f_input().rstrip().split())
    print(a, b, c)

