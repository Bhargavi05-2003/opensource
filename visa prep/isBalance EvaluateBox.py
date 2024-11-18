N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    left_weight = sum(A[:i])
    right_weight = sum(A[i+1:])
    balance = abs(left_weight - right_weight)
    B.append(balance)
print(*B)
