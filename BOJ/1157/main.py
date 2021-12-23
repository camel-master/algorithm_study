import sys
s = sys.stdin.readline().rstrip()
# A:65, a:97
counter_list = [0] * 26
for e in s:
    if ord(e) >= 65 and ord(e) <= 65+26:
        counter_list[ord(e) - 65] += 1
    if ord(e) >= 97 and ord(e) <= 97+26:
        counter_list[ord(e) - 97] += 1
max_count = max(counter_list)
if counter_list.count(max_count) > 1:
    print('?')
else:
    print(chr(counter_list.index(max_count) + 65))
