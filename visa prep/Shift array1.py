def rotate_array(arr, n):
    return arr[1:] + [arr[0]]
n = int(input())
arr = list(map(int, input().split()))
rotated_arr = rotate_array(arr, n)
print(" ".join(map(str, rotated_arr)))
