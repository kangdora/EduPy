# 메모리 제한이 1gb임.
# 구현같은 느낌. 대신 시간복잡도 조심해서
# 시간복잡도만 보면 이분탐색일지도?
# 아마 시뮬돌려도 될거같긴함. lst[1] 기준 정렬해서 풀면 되나?
# 아무리 해도 너무 깔끔한 코드가 아니어서 다른 로직을 생각해보니까, 우선순위큐로 구현 가능해보임.

import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())

arr_heap = []
reserve_at = {}
t2_lst = [0] * N

for i in range(N):
    t1, t2 = map(int, input().split())
    heapq.heappush(arr_heap, (t2, t1, i))  # 도착시간, 예약시간, id
    reserve_at[t1] = i
    t2_lst[i] = t2

q = deque()
arrived = [False] * N  # 도착 여부
joined = [False] * N  # 입장 여부

time = 0
joined_cnt = 0
ans = 0

while joined_cnt < N:
    time += 1

    while arr_heap and arr_heap[0][0] == time:
        t2, t1, person_id = heapq.heappop(arr_heap)
        arrived[person_id] = True
        q.append(person_id)

    flag = False
    reverse_id = reserve_at.get(time)

    if reverse_id is not None and arrived[reverse_id] and not joined[reverse_id]:
        joined[reverse_id] = True
        joined_cnt += 1
        wait = time - t2_lst[reverse_id]
        if wait > ans:
            ans = wait
        flag = True

    if not flag:
        while q and joined[q[0]]:
            q.popleft()
        if q:
            person_id = q.popleft()
            if not joined[person_id]:
                joined[person_id] = True
                joined_cnt += 1
                wait = time - t2_lst[person_id]
                if wait > ans:
                    ans = wait

print(ans)
