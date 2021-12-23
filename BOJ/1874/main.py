"""
BOJ 1874 스택 수열

"""
n = int(input())
counter = 1
stack = list()
operations = list()
num_list = list()
stackable = True
for _ in range(n):
    num_list.append(int(input()))
for num in num_list:
    while True:
        if not stack:
            stack.append(counter)
            operations.append('+')
            counter += 1
        else:
            if stack[-1] > num:
                stackable = False
                break
            if num <= stack[-1]:
                pop_data = stack.pop()
                operations.append('-')
                if num == pop_data:
                    break
            else:
                stack.append(counter)
                operations.append('+')
                counter += 1
    if not stackable:
        break

if not stackable:
    print('NO')
else:
    for op in operations:
        print(op)
