"""
BOJ 1138 단어 만들기
단어를 구성한 문자들과 퍼즐판을 구성한 문자의 개수가 A ~ Z 까지 각각 모두 몇개 씩인지 카운팅 한다.

단어들을 구성하는 문자들의 종류별 카운팅에 필요한 최대 연산 회수는 다음과 같다.
단어의 수 * 단어 최대 길이 = 20만 * 9 = 180만
단어별로 문자 수를 카운팅한 정보는 다음과 같이 만든다.
{
    'APPLE': {'A': 1, 'P':2, 'L': 1, 'E': 1},
    'BANANA': {'A': 3, 'B': 1, 'N': 2}
    ...
}

퍼즐판 내용을 딕셔너리 형태로 만들어 둔다.
만약 퍼즐판이 LARBITNLI와 같이 주어진 경우
p_alpha = {'L': 2, 'A': 1, 'R': 1, 'B': 1, 'I': 2, 'T': 1, 'N': 1}
각 단어들이 퍼즐판 내용으로 완성 가능한지 확인한다.

단어를 구성하는 각 알파벳의 수와 p_alpha의 각 알파벳 수를 각각 비교하여 단어의 모든 구성 알파벳 수가
p_alpha 이하인 경우는 퍼즐을 통해 구성할 수 있는 단어가 된다.
구성할 수 있는 단어의 경우 combinable = set() 에 넣어두자.


퍼즐을 통해 구성할 수 있는 단어인 경우 단어를 구성하는 알파벳 수량만큼 알파벳별 누적 값에 더해간다.
acc_alpah = {'L': 0, 'A': 0, 'R': 0, 'B': 0, 'I': 0, 'T': 0, 'N': 0}

모든 단어에 대해 구성 알파벳의 수량을 알파벳 누적 값에 적용한 후 가장 출현 빈도가 낮은 알파벳들과
가장 출현빈도가 높은 알파벳들을 골라내서 출력한다.
이후 combinable set에서 하나씩 원소를 꺼내 각각 출연빈도가 낮은 알파벳을 포함하는 경우와
출연빈도가 높은 알파벳을 포함하는 경우의 개수를 카운딩한다.
"""
import sys
f_input = sys.stdin.readline

words = list()
puzzles = list()
while True:
    word = f_input()
    if word == '-':
        break
    words.append(word)

while True:
    puzzle = f_input()
    if puzzle == '#':
        break
    puzzles.append(puzzle)

words_dict = dict()
for word in words:
    words_dict[word] = dict()
    for ch in word:
        if ch in words_dict[word]:
            words_dict[word][ch] += 1
        else:
            words_dict[word][ch] = 1

for puzzle in puzzles:
    combinable_words = set()
    p_alpha = dict()
    acc_alpha = dict()
    p_alpha[puzzle] = dict()
    acc_alpha[puzzle] = dict()
    # 퍼즐 별로 각각의 문자들이 몇번 등장하는지 카운팅한다.
    for ch in puzzle:
        if ch in p_alpha[puzzle]:
            p_alpha[puzzle][ch] += 1
        else:
            p_alpha[puzzle][ch] = 1
        # 퍼즐 요소로 조합할 수 있는 모든 단어들을 순회하면서 각 문자들의 등장 누계를 기록할 딕셔너리를 초기화 한다.
        acc_alpha[puzzle][ch] = 0

    # 주어진 단어들이 퍼즐의 문자들로 조합할 수 있는 지 확인한다.
    for word in words:
        is_contained = True
        for key in words_dict[word].keys():
            if key not in p_alpha[puzzle] or p_alpha[puzzle][key] < words_dict[word][key]:
                is_contained = False
                break
        # 조합할 수 있으면
        if is_contained:
            # 별도의 집합에 해당하는 단어를 보관하고
            combinable_words.add(word)
            # 등장 문자 누계를 업데이트 한다.
            for key in words_dict[word].keys():
                acc_alpha[puzzle][key] += 1

    # 등장 문자 누계를 오름차순 정렬한다.
    p_items = acc_alpha[puzzle].items()
    p_items = sorted(p_items, key=lambda x: (x[1], x[0]))

    # 가장 낮은 빈도의 문자들과, 가장 높은 빈도의 문자들을 추출한다.
    min_cnt = p_items[0][1]
    max_cnt = p_items[-1][1]
    min_str = ''
    max_str = ''
    for item in p_items:
        if min_cnt == item[1]:
            min_str += item[0]
        if max_cnt == item[1]:
            max_str += item[0]

    # 가장 낮은 빈도의 문자가 포함된 단어들의 수와 가장 높은 빈도의 문자가 포함된 단어들의 수를 추출한다.
    min_w_cnt = 0
    max_w_cnt = 0
    for cw in combinable_words:
        if p_items[0][0] in cw:
            min_w_cnt += 1
        if p_items[-1][0] in cw:
            max_w_cnt += 1

    print(min_str, min_w_cnt, max_str, max_w_cnt)
