def subSet(idx, S):
    if idx == len(st):
        arr.append(S)
        return
    subSet(idx + 1, S + st[idx])
    subSet(idx + 1, S)


st = "ab"
arr = []
subSet(0, "")
print(arr)
