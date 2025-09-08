# 대충 투포인터 아닐까
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

left_idx, right_idx = 0, n - 1

ans = abs(lst[left_idx] + lst[right_idx])
ans_left, ans_right = left_idx, right_idx

while left_idx < right_idx:
    tmp = lst[left_idx] + lst[right_idx]

    if abs(tmp) < ans:
        ans_left = left_idx
        ans_right = right_idx
        ans = abs(tmp)

        if ans == 0:
            break

    if tmp < 0:
        left_idx += 1

    else:
        right_idx -= 1

print(lst[ans_left], lst[ans_right])