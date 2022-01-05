"""
BOJ 1620 나는야 포켓몬 마스터 이다솜
https://www.acmicpc.net/problem/1620

N: 포케몬의 개수
M: 문제 개수
1 <= N, M <= 100,000를 만족하는 자연수

포케몬의 이름을 p_name이라 할 때 2 <= len(p_name) <= 20

문제를 해결하기 위해 입력받는 N개의 포케몬 도감 데이터를 {포케몬 이름: 번호}, {번호: 포케몬 이름} 형태의 두 가지 딕셔너리로 만들어 놓고
M개의 문제 중에 숫자타입으로 변환가능한 문자인 경우는 {번호: 포케몬 이름}에서 결과를 찾아 출력하고,
숫자타입으로 변환이 불가한 경우 {포케몬 이름: 번호}에서 결과를 찾아 출력한다.

입력된 포케몬 도감 데이터를 딕셔너리 두개로 바꿔야 하므로 도감 데이터 작성에 대한 시간 복잡도는 O(N * 2)이고 상수항을 무시하면 O(N)이다.

str 타입의 isdigit() 을 사용하여 문제의 입력 값이 숫자인지 문자인지 확인한다.
isdigit()의 시간복잡도는 적어도 선형시간이 들어갈 것으로 예상된다. 따라서 시간 복잡도는 O(M * 20)이고 상수항을 무시하면 O(M)에 처리가
가능하다.

단순히 딕셔너리 두개를 사용해 처리를 시도할 경우 시간복잡도는 문제를 푸는데 지장이 없을 것으로 보인다.

파이썬에서 sys.getsizeof()를 사용하여 확인해보면 문자 한개는 1byte씩이므로
20글짜씩 꽉 채워 N개의 포케몬 도감을 작성한다면 공간복잡도는 O((20 * N + 4)*2) 가 된다.
최대로 공간을 사용한다고 가정하면 3.8MB 정도 사용하게 될것이므로 공간 복잡도도 문제가 없다.

[참고용 코드]
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    pkmn = []
    pkmn_dic = {}
    res = []
    for i in range(1,n+1) :
        pk = input().rstrip()
        pkmn.append(pk)
        pkmn_dic[pk] = i
    for _ in range(m):
        query = input().rstrip()
        if query.isdigit() :
            res.append(pkmn[int(query)-1])
        else :
            res.append(str(pkmn_dic[query]))
    print('\n'.join(res))

if __name__=='__main__':
    solve()
"""
import sys
f_input = sys.stdin.readline


N, M = map(int, f_input().rstrip().split())
num_to_name = dict()
name_to_num = dict()
for i in range(1, N + 1):
    pm_name = f_input().rstrip()
    num_to_name[str(i)] = pm_name
    name_to_num[pm_name] = str(i)

for _ in range(M):
    question = f_input().rstrip()
    if question.isdigit():
        print(num_to_name[question])
    else:
        print(name_to_num[question])
