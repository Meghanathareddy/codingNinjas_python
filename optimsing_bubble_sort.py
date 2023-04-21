def optimise_buuble_sort(arr, n):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j]> arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
n = int(input())
arr = list(map(int, input().split(' ')))
optimise_buuble_sort(arr, n)
print(*arr)