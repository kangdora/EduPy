# bfs
# 0,0부터 bfs 돌려서, ex: 바깥 공기와 맞닿은 1(치즈) 리스트를 모음.
# ex를 0으로 녹이고, 그 좌표들을 다음 라운드 시작점으로 사용.

import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    q = deque()
    ex = []
    seen = set()

    for y, x in lst:
        if 0 <= y < h and 0 <= x < w and not visited[y][x]:
            visited[y][x] = True
            q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if graph[ny][nx] == 1:
                    if (ny, nx) not in seen:
                        seen.add((ny, nx))
                        ex.append((ny, nx))
                else:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))
    return ex

res = [(0, 0)]
cnt = 0
last = 0

while res := bfs(res):
    last = len(res)
    for y, x in res:
        graph[y][x] = 0
    cnt += 1

print(cnt)
print(last)