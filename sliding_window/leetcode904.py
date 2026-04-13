fruits = [1, 2, 3, 2, 2]
left, right, count, max_count = 0, 0, 0, 0
hash = {}
while right < len(fruits):
    hash[fruits[right]] = 1 + hash.get(fruits[right], 0)
    print(hash)
    count += 1

    if len(hash) > 2:
        hash[fruits[left]] -= 1
        count -= 1
        if hash[fruits[left]] == 0:
            hash.pop(fruits[left])
        else:
            left += 1
    max_count = max(max_count, count)
    right += 1
print(max_count)
