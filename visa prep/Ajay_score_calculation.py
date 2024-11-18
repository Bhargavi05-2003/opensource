def calculate_score(X, N):
    points_per_test_case = X // 10  
    score = points_per_test_case * N  
    return score
T = int(input())
for _ in range(T):
    X, N = map(int, input().split())
    
    print(calculate_score(X, N))
