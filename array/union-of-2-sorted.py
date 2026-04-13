nums1,nums2 = [1,5,5,9,9,12],[0,0,2,2,4,8,9]
a = []
i,j = 0,0
a.append(min(nums1[0],nums2[0]))

while i<len(nums1) and j<len(nums2):
    if nums2[j]<nums1[i]:
        if nums2[j]>a[-1]:
            a.append(nums2[j])
        j+=1
    else:
        if nums1[i] > a[-1]:
            a.append(nums1[i])
        i+=1
while i<len(nums1):
    a.append(nums1[i])
    i+=1
while j < len(nums2):
    a.append(nums2[j])
    j+=1
print(a)    
