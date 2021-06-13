# Program to reverse an array

def reverse_array(arr):
    begin = 0
    end = len(arr)-1

    while begin < end:
        try:
            arr[begin], arr[end] = arr[end], arr[begin]
            begin += 1
            end -= 1

        except Exception as err:
            print(err, begin, end)
            break

    return arr


arr = list(map(int, input().split(' ')))
print(reverse_array(arr))