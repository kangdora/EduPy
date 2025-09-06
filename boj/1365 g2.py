# 이분 탐색 + LIS 문제
# 많이 쓰이는 유형인거 같은데 발상이 독특하다.
# 결론은 DP인데, DP같은 점화식 구현을 좀 더 효율적으로 한 느낌
import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = map(int, input().split())
lis = []

for x in arr:
    i = bisect.bisect_left(lis, x)
    if i == len(lis):
        lis.append(x)
    else:
        lis[i] = x

print(n - len(lis))
