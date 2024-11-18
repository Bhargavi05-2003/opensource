def reverse_integer(n):
    INT_MIN,INT_MAX = -2**31, 2**31 - 1
    sign = -1 if n<0 else 1
    reversed_number = int(str(abs(n))[::-1])
    reversed_number *= sign
    if reversed_number < INT_MIN or reversed_number > INT_MAX:
        return 0
    return reversed_number
n = int(input())
print(reverse_integer(n))
