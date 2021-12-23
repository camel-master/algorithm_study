"""
BOJ 10814 나이순 정렬
https://www.acmicpc.net/problem/10814

가입순서에 대한 정보가 주어지지 않기 때문에, 나이 순으로 정렬 할 때
안정정렬이 되어야 동일 나이에 대해 가입순서대로 정렬 되는 것이 보장된다.
N의 범위가 1 <= N <= 100,000

python의 sort()는 안정정렬이고 시간복잡도는 O(n log n)이다.
또한 100,000개의 데이터라고 가정 했을 때 800,000byte 이므로
메모리 제한도 준수할 수 있다.

"""
import sys
f_input = sys.stdin.readline


N = int(f_input())
user_list = list()
for _ in range(N):
    age, name = f_input().rstrip().split()
    user_list.append((int(age), name))

user_list.sort(key=lambda x:x[0])
for user in user_list:
    print(user[0], user[1])
