"""
BOJ 5525 IOIOI
https://www.acmicpc.net/problem/5525

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)

제한
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
S는 I와 O로만 이루어져 있다.

Pn이 S에 몇번 들어가 있는지 확인.

입력 예를 살펴보자.
N = 1
M = 13
S = OOIOIOIOIIOII

우선 Pn에 해당하는 문자열을 만든다.
Pn = 'IOI'

S의 시작점 부터 Pn을 맞춰가며 Pn이 들어 있는지 확인한다.
OOIOIOIOIIOII
IOI

OOIOIOIOIIOII
 IOI

OOIOIOIOIIOII
  IOI           (OK)

OOIOIOIOIIOII
   IOI

OOIOIOIOIIOII
    IOI         (OK)

OOIOIOIOIIOII
     IOI

OOIOIOIOIIOII
      IOI       (OK)

OOIOIOIOIIOII
       IOI

OOIOIOIOIIOII
        IOI

OOIOIOIOIIOII
         IOI    (OK)

OOIOIOIOIIOII
          IOI

S를 선형으로 탐색하면서 len(Pn)만큼의 범위가 Pn인지 확인한다.
len(S) = 10 이고 P1이라면
    (M - (2P + 1) + 1) * (2P + 1) 만큼 탐색해야 하므로 = 8 * 3 = 24만큼 탐색해야 한다.

M = 1000000이고, N = 1이면
    (1000000 - 2) * 3

M = 1000000이고, N = 10이면
    (1000000 - 20) * (10 + 1)

O((M - (2N + 1)) * (2N + 1))
2N + 1 = A 라 해보면 O((M - A) * A) = O(MA - A^2) = O(2NM + 2AN)

만약 N = 1000, M = 1000000 정도만 되더라도 연산 회수가 20억 가량 될 수가 있다.
따라서 제한시간을 초과하게 된다.

다음과 같이 알고리즘을 수정해보고자 한다.

while current index <= M - (2N + 1)
    if current index의 문자 == I then counter = 0
        while S[index + 1] == O and S[index + 1] == I:
            index += 2
            counter = count + 1
        if counter >= len(Pn) then 결과에 counter - len(Pn) + 1 만큼 더해준다.

S를 선형으로 탐색하면서 IOIOI.... 형태의 부분 문자열의 길이를 구해내고 그 안에서 Pn이 몇번이나
등장하는지 카운팅 한다.
위의 알고리즘은 O(n)으로 돌기에 문제에 제시된 시간 제한을 충분히 통과할 수 있다.

공간복잡도를 보자면 문자열을 최대로 저장했을 때 약 1mb 그 상태에서 IOIIOIIOI... 와 같이
S가 구성되어 있다고 하면 Counter list를 저장하는데 1.3mb 가량이 소요되므로 공간복잡도 역시
문제의 제한사항을 통과할 수 있다.

1
9
IIOOIIOOI

expected: 0


참고할만한 코드
N = int(input())
M = input()
S = input().replace('IO','X').replace('XI','XXO').replace('I','O').split('O')
count = 0
for s in S:
  count += max(len(s) - N, 0)
print(count)
"""
import sys
f_input = sys.stdin.readline


N = int(f_input())
M = int(f_input())
S = f_input().rstrip()

curr_idx = 0
cnt_list = list()
while curr_idx <= M - (2 * N + 1):
    if S[curr_idx] == 'I':
        cnt = 0
        if S[curr_idx+1] != 'O' or S[curr_idx+2] != 'I':
            curr_idx += 1
            continue
        while S[curr_idx+1] == 'O' and S[curr_idx+2] == 'I':
            cnt += 1
            curr_idx += 2
            if curr_idx > (M - 3):
                curr_idx += 1
                break
        if cnt >= N:
            cnt_list.append(cnt)
    else:
        curr_idx += 1
res = 0
for cnt in cnt_list:
    res += cnt - N + 1
print(res)

