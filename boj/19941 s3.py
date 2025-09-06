# 그리디 문제

# 보통 정렬이 없으면 dp 문제일 확률이 줄어듬
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(input().rstrip())
q: deque[tuple[int, str]] = deque()  # 내 생각에 이 부분에서 왜 이렇게 썼는지 궁금할 수 있는데
ans = 0


def find(lst, ch):
    length = len(lst)

    if ch == "H":
        for i in range(length):
            if lst[i][1] == "P":
                return i + 1
    elif ch == "P":
        for i in range(length):
            if lst[i][1] == "H":
                return i + 1
    return False

for idx, ch in enumerate(lst):
    if q and idx - q[0][0] > m:
        q.popleft()

    tmp = find(q, ch)

    if tmp:
        del q[tmp - 1]
        ans += 1
    else:
        q.append((idx, ch))

print(ans)