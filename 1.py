# Add sum of numbers in an array

def add_sum(arr):
    s = 0
    for num in arr:
        s += num

    return s


arr = list(map(int, input().split()))
print(add_sum(arr))