N = int(input())
counter = 1
for i in range(1, N+1):
    for j in range(i):
        print(counter, end=" ")
        counter += 1
    print()
