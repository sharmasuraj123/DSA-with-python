nums = [1, 2, 1, 3, 2, 5]
xor_nums = 0
for i in nums:
    xor_nums^=i
print(xor_nums)    
odd_bit_position = 1    
while xor_nums:
    if xor_nums%2!=0:
        break
    xor_nums>>=1
    odd_bit_position+=1
print(odd_bit_position)    
    
a,b = 0,0
for i in nums:
    x = i>>odd_bit_position-1 
    if x%2==0:a^=i
    else: b^=i
print([a,b])
