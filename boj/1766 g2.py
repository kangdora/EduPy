# 유향 그래프 문제
# 아마 N이 32000이라 배열로 풀기는 쉽지 않아보임.
# 인접 리스트 방식으로 구현하면 가능할듯?
# 인접 리스트 방식에다가 우선순위큐를 넣어서 빼면 n log n
# 딱 위상정렬이구나

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indeg[b] += 1

heap = [i for i in range(1, n + 1) if indeg[i] == 0]
heapq.heapify(heap)

ans = []
while heap:
    u = heapq.heappop(heap)
    ans.append(u)
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            heapq.heappush(heap, v)

print(*ans)
