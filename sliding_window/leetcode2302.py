nums = [5, 2, 6, 8, 9, 7]
k = 50
l, r, count, n = 0, 0, 0, len(nums)
sum,size = 0,0
while r < n:
    print("s")
    sum += nums[r]
    size = r-l+1

    while sum*size >= k and l <= r:
        sum -= nums[l]
        l += 1
        size=r-l+1

        if sum*size < k:
            break
    count += (r - l + 1)
    print(count)
    r += 1
    print("end")
print(count)
