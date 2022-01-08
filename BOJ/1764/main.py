"""
BOJ 1764
https://www.acmicpc.net/problem/1764

0 <= N, M <= 500000
각 문자열의 길이는 20 이하.

N개의 문자열을 저장하는데 set type을 사용하면
문자열이 존재하는지 확인하는데 O(1)의 시간복잡도이다.
따라서 M개의 문자열이 N개의 원소를 가진 문자열 집합에
들어있는지 확인하면 되므로 O(M)의 시간복잡도가 된다.
제한시간이 2초에 50만번 연산이므로 충분히 수행가능하다.

메모리 제한은 256MB이고 N개의 데이터를 저장하고 있어야 하므로
최대로 많이 데이터를 저장하는 경우 50000 * 20 = 1000000 byte
약 1MB를 사용하므로 수행가능한 알고리즘이다.

참고 코드
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

names = set()
for _ in range(N):
    names.add(input().rstrip())

p_names = list()
for _ in range(M):
    search_name = input().rstrip()
    if search_name in names:
        p_names.append(search_name)
print(len(p_names))
p_names.sort()
for p_name in p_names:
    print(p_name)
