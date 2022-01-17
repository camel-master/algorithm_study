"""
Programmers 2020 KAKAO BLIND RECRUITMENT 신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334

id를 key로 Value는 신고한 유저의 집합을 가진 딕셔너리를 만들어서 처리해보도록 한다.
{id: {신고자 id 1, 신고자 id 2, ...}



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

"""
def solution(id_list, report, k):
    answer = []
    reported_users = dict() # 신고당한 횟수
    users = dict()  # 신고한 유저들을 집합구조로 저장.
    for id in id_list:
        reported_users[id] = set()
        users[id] = set()

    for r in report:
        uid, reported_id = r.split()
        reported_users[reported_id].add(uid)
        users[uid].add(reported_id)

    for repo_info in users.items():
        cnt = 0
        for repo_id in repo_info[1]:

            if len(reported_users[repo_id]) >= k:
                cnt += 1
        answer.append(cnt)

    return answer
