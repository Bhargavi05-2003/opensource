def difference_between_sums(n,m,arr):
    num1 = sum(x for x in arr if x % m != 0)
    num2 = sum(x for x in arr if x % m == 0)
    return num2 - num1
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(difference_between_sums(n,m,arr))
