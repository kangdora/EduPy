# 시간 복잡도 계산
# N 최대 100, K 최대 200, A_i 최대 1000
# 모든 칸 1000 기준 한 과정당 2N만큼 소요.
# 1000 * 200 * 100 걍 시뮬인듯? 알고리즘은 따로 떠오르지 않음.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

robot = [False] * (2 * N)
st_pos = 0
ed_pos = N - 1
cnt = 0
idx = 0

while True:
    idx += 1

    # 1
    st_pos = (st_pos - 1) % (2 * N)
    ed_pos = (ed_pos - 1) % (2 * N)
    if robot[ed_pos]:
        robot[ed_pos] = False

    # 2
    for i in range(N - 2, -1, -1):
        cur = (st_pos + i) % (2 * N)
        nxt = (cur + 1) % (2 * N)
        if robot[cur] and not robot[nxt] and A[nxt] > 0:
            robot[cur] = False
            if nxt != ed_pos:
                robot[nxt] = True
            A[nxt] -= 1
            if A[nxt] == 0:
                cnt += 1
    if robot[ed_pos]:
        robot[ed_pos] = False

    # 3
    if A[st_pos] > 0 and not robot[st_pos]:
        robot[st_pos] = True
        A[st_pos] -= 1
        if A[st_pos] == 0:
            cnt += 1

    # 4
    if cnt >= K:
        print(idx)
        break