"""
BOJ 5430 AC
https://www.acmicpc.net/problem/5430

배열의 데이터를 reverse 해가면서 pop하도록 하는 알고리즘을 작성해야한다.
리스트 대신 양 끝단의 데이터를 pop하는데 O(1)의 시간복잡도인 deque을
사용하여 데이터를 저장한다.
방향성을 저장할 변수 하나를 사용하여 변수 값에 따라 popleft() 또는 pop()으로
데이터를 pop해나간다.
T = 테스트 케이스, 1 <= T <= 100
p = 수행할 함수 1 <= p <= 100,000
n = 데이터 수
nums = 처리할 데이터 각 데이터의 범위는 1 <= nums[i] <= 100

시간복잡도
O(T * p)로 최대 100 * 100000 = 10,000,000번 연산 하므로 제한시간 1초 내로 수행가능

공간복잡도
n개의 정수 데이터를 저장하고 있어야 하므로 O(n)이다. 따라서 최대 100,000 * 4 byte
약 390kb로 처리 가능하므로 메모리 제한 256mb를 통과할 수 있다.

5
R
1
[1]
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
R
0
[]



5
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
R
1
[1]

참고할 코드
for _ in range(int(input())):
    f=list(map(len,input().replace('RR','').split('R')))
    n=int(input())
    a=input()[1:-1].split(',')
    s,e=sum(f[0::2]),n-sum(f[1::2])
    a=a[s:e] if len(f)%2==1 else a[s:e][::-1]
    print(f"[{','.join(a)}]" if s<=e else "error")
"""
from collections import deque
import sys

f_input = sys.stdin.readline

T = int(f_input().rstrip())
for i in range(T):
    p = f_input().rstrip()
    n = int(f_input().rstrip())
    nums = deque()
    if n > 0:
        nums = deque(list(map(int, f_input().rstrip()[1:-1].split(','))))
    else:
        f_input().rstrip()
        nums = deque()
    data_flow = 1   # 1:left to right, -1:right to left
    is_error = False
    for inst in p:
        if inst == 'R':
            data_flow *= -1
        if inst == 'D':
            if not nums:
                is_error = True
                break
            if data_flow == 1:
                nums.popleft()
            else:
                nums.pop()
    if not is_error:
        if data_flow == -1:
            nums = deque(list(nums)[-1::-1])
            print('[' + ','.join(map(str, nums)) + ']')
        else:
            print('[' + ','.join(map(str, nums)) + ']')
    else:
        print('error')
