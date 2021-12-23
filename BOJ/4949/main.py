"""
BOJ 4949 균형잡힌 세상
https://www.acmicpc.net/problem/4949

대괄호 [], 소괄호 () 모두 괄호가 열리고 닫히는 짝이 맞도록 문자열이 주어지면 yes를
그렇지 않으면 no를 출력하도록 한다.
stack을 사용해보도록 하자.
닫히는 괄호를 만나면 stack에 쌓고 열리는 괄호를 만났을 때 동일 타입의 괄호인 경우 pop한다.
동일 타입의 괄호가 아니라면 균형잡힌 괄호가 아니므로 문자열을 더이상 확인하지 않고 no를 출력한다.
모든 문자열에 대해 확인하는 동안 균형잡히지 않은 괄호 문자열이 아닌 경우가 없었다면 yes를 출력한다.
"""
import sys
f_input = sys.stdin.readline

parentheses = {']': '[', ')': '('}
while True:
    string = f_input().rstrip()
    if string == '.':
        break

    stack = list()
    for ch in string:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == ']' or ch == ')':
            if not stack:
                stack.append(ch)
                break
            else:
                if stack[-1] == parentheses[ch]:
                    stack.pop()
                else:
                    break
    if stack:
        print('no')
    else:
        print('yes')
