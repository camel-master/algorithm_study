"""
집합 타입에 초기 값으로 원소 666을 추가한다.
0 ~ n +  666 + 0 + n 의 형태로 숫자를 구성하여 집합에 추가한다.
prefix + 666 + suffix
len(prefix) x len(suffix)의 개수만큼 숫자 생성 된다.
666을 포함하는 숫자의 총 개수는 10,000개 이하이다.
총 4개의 숫자가 앞뒤로 나뉘어 추가될 수 있다고 해보자.

666  = 1
if len = 0 then total = 1

x666 = 10
666x = 10
if len = 1 then total = 20

xx666 = 100
666xx = 100
x666x = 100
if len = 2 then total 300

xxx666 = 1000
xx666x = 1000
x666xx = 1000
666xxx = 1000
if len = 3 then total 4000

xxxx666 = 10000
xxx666x = 10000
xx666xx = 10000
x666xxx = 10000
666xxxx = 10000
if len = 4 then total 50000

따라서 앞 뒤로 추가될 수 있는 숫자의 최고 길이는 4개가 된다.

---------------------풀이완료---------------------------
N == 10,000 이므로 666 앞,뒤에 추가되는 숫자의 개수가 적어도 4개는 되어야 한다.

먼저 '666' 앞에 붙여질 숫자들을 prefix라 하자.
일단 아무 것도 붙지 않는 경우가 있다. 즉, prefix는 공백일 수 있다.
다음으로 숫자 1 ~ 9999까지가 붙을 수 있다. 따라서 prefix는 ['', '1', '2', ... '9999']까지가 될 수 있다.

'666' 뒤에 붙여질 숫자들을 suffix라 하자.
suffix는 prefix와 다르게 '0000'같은 형태도 인정해줘야 한다. 또한 prefix의 길이 즉 앞에 붙여진 숫자의 개수에 따라
suffix의 길이가 제한된다. 예를 들어 prefix의 길이가 1이면 suffix의 길이 <= (4 - prefix 길이)를 만족하는 suffix만
붙을 수 있다.
=> prefix == '1' 일 때를 보자면 다음과 같이 suffix가 붙을 수 있다.
    '1' + '666' + ''        (가능)
    '1' + '666' + '0'       (가능)
    '1' + '666' + '00'      (가능)
    '1' + '666' + '000'     (가능)
    '1' + '666' + '0000'    (불가능: prefix 길이 + suffix 길이가 4를 초과하기 때문에)

"""
from itertools import product

N = int(input())
n_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = set()
temp = [n_chars for _ in range(4)]
prefixes = list()
for p in product(*temp):
    prefix = str(int(''.join(p)))
    if prefix != '0':
        prefixes.append(prefix)
    else:
        prefixes.append('')

for prefix in prefixes:
    suffix_len = 4 - len(prefix)
    for sl in range(suffix_len, -1, -1):
        temp = [n_chars for _ in range(sl)]
        numbers.add(int(prefix + '666'))
        for p in product(*temp):
            suffix = ''.join(p)
            numbers.add(int(prefix + '666' + suffix))

numbers = list(numbers)
numbers.sort()
print(numbers[N-1])