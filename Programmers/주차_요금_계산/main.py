"""
Programmers 주차 요금 계산
https://programmers.co.kr/learn/courses/30/lessons/92341

차량 번호별 누적 주차 시간을 구한다.
기본 요금을 부과하고 누적 주차 시간에서 기본시간을 차감한다.
if 누적 주차 시간 > 0에 한해 올림하여 추가요금을 부과한다.
차량 번호 오름차순으로 주차 요금을 출력한다.
"""
import heapq
import math


def solution(fees, records):
    # fees index: 0: 기본시간, 1: 기본요금, 2: 단위시간, 3: 단위요금
    # 들어오는 차량 번호별로 시각을 minheap에 넣어둔다. 시각은 시간 + 분/60 형태로 저장한다.
    # 나가는 차량 번호별로 마찬가지로 시각을 딕셔너리 타입에 저장한다.
    costs = list()
    in_records = dict()
    out_records = dict()
    for record in records:
        time, car_num, in_out = map(str, record.split())
        time = time.split(':')
        minute = int(time[0]) * 60 + int(time[1])
        if in_out == 'IN':
            if not in_records.__contains__(car_num):
                in_records[car_num] = list()
            heapq.heappush(in_records[car_num], minute)
        if in_out == 'OUT':
            if not out_records.__contains__(car_num):
                out_records[car_num] = list()
            heapq.heappush(out_records[car_num], minute)
    # print(in_records)
    # print(out_records)
    for car_num in sorted(list(in_records.keys())):
        acc_time= 0
        while in_records[car_num]:
            in_time = heapq.heappop(in_records[car_num])
            out_time = float()
            if not out_records.__contains__(car_num) or not out_records[car_num]:
                out_time = 23 * 60 + 59
            else:
                out_time = heapq.heappop(out_records[car_num])
            acc_time += out_time - in_time
        # print(acc_time)
        cost = fees[1]
        acc_time -= fees[0]
        if acc_time > 0:
            cost += math.ceil(acc_time / fees[2]) * fees[3]
        costs.append(cost)
        # print(car_num, cost)

    return costs


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
