arr = [4, 9, 2, 5, 1]
k = 10


def backtrack(arr, k, idx):
    if k == 0:
        return 1
    if k < 0 or idx == len(arr):
        return 0
    return backtrack(arr, k - arr[idx], idx + 1) + backtrack(arr, k, idx + 1)


result = backtrack(arr, k, 0)
print(result)
