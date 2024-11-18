A, B, C = map(int, input().split())
max_capacity = C - B
max_mangoes = 0
while(B + (max_mangoes + 1) * A) <= C:
    max_mangoes += 1
print(max_mangoes)
