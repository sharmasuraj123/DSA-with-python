# brute force approch.

# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# total_water = 0
# for i in range(len(height)):
#     left,right = height[:i],height[i+1:len(height)]
#     left_max,right_max = height[i],height[i]
#     for j in left:
#         if j>left_max:
#             left_max=j
#     for j in right:
#         if j > right_max:
#             right_max = j
#     min_val = min(left_max,right_max)
#     if height[i]<min_val:
#         total_water+=(min_val-height[i])
# print(total_water)

height = [4, 2, 0, 3, 2, 5]
n = len(height)
total_water = 0
left_max_arr, right_max_arr = [0] * n, [0] * n
left_max_arr[0] = height[0]
right_max_arr[n-1] = height[n-1]
for i in range(1,n):
    left_max_arr[i] = max(left_max_arr[i-1], height[i])
for i in range(n-2,-1,-1):
    right_max_arr[i] = max(right_max_arr[i+1], height[i])
for i in range(n):
    min_val = min(left_max_arr[i],right_max_arr[i])
    if height[i]<min_val:
        total_water+=(min_val-height[i])
print(total_water)    
