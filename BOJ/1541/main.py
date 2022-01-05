"""
BOJ 1541 잃어버린 괄호
https://www.acmicpc.net/problem/1541
수식 문자열을 formula라고 하자.
양수와 음수를 각각 저장할 두 리스트 positive, negative 를 선언한다.
선형탐색 하면서 처음 시작되는 숫자에 해당하는 부분 문자열을 숫자타입으로 변경하여 positive에 넣는다.
+ 이후의 숫자에 해당하는 부분 문자열을 숫자타입으로 변경하여 positive에 넣는다.
한번이라도 -를 만나면 이후의 모든 숫자를 negative에 넣는다.


"""

formula = input()
positive = list()
negative = list()
curr_sign = '+'
num = ''
for ch in formula:
    if ch == '+' or ch == '-':
        if curr_sign == '-':
            negative.append(int(num))
        else:
            positive.append(int(num))
        if ch == '-':
            curr_sign = '-'
        num = ''
    else:
        num += ch
if curr_sign == '-':
    negative.append(int(num))
else:
    positive.append(int(num))

print(sum(positive) - sum(negative))
