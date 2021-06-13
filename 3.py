# Sorting using quick sort

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)


def partition(arr, left, right):
    i = left - 1
    j = left

    while j < right:
        if arr[j] <= arr[right]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


arr = list(map(int, input().split(' ')))
quick_sort(arr, 0, len(arr)-1)
print(arr)