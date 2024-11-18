A, B, C = map(int, input().split())
total_time_needed = A * B
available_time = C * 24 * 60
if total_time_needed <= available_time:
    print("YES")
else:
    print("NO")
