start,goal = 10,7
bit_count = 0
while start or goal:
    bit1 = start%2 if start else 0
    bit2 = goal%2 if goal else 0
    if bit1!=bit2:bit_count+=1
    start = start>>1
    goal = goal>>1
print(bit_count) 