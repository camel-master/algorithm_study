"""
BOJ 10989 수 정렬하기 3

메모리 제한이 8MB이다.
10,000,000개의 리스트 공간이 필요하므로 각 공간에 정수타입의 데이터가 저장된다고 했을 때
40,000,000 byte의 공간을 필요로 한다. 이는 약 40MB를 필요로 하므로 다른 방법으로 접근해야 한다.

이를 해결하기 위해 계수 정렬을 사용해보도록 하자.
1 ~ 10,000를 인덱스로 갖는 딕셔너리를 선언하고 각 인덱스에 해당하는 데이터가 나올 떄마다 1씩
더해간다.
이후 인덱스 순서 별로 해당 인덱스의 값만큼 인덱스 숫자를 출력해준다.
"""
from collections import defaultdict
import sys
f_input = sys.stdin.readline

N = int(f_input())
numbers = defaultdict(int)
for _ in range(N):
    num = int(f_input())
    numbers[num] += 1

numbers = sorted(numbers.items(), key=lambda x: x[0])
for number in numbers:
    for cnt in range(number[1]):
        print(number[0])
