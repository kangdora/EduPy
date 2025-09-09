# 누가봐도 분리 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
ans = [(0, 0)] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)
    idx = find(x)
    cur, summery = ans[idx]
    ans[idx] = summery * lst[y - 1] + cur, summery + lst[y - 1]
    print(ans[idx][0])