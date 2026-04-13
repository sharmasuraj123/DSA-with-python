val, wt, capacity = [8,2,10,1,9,7,2,6,4,9], [10,1,7,7,5,1,8,6,8,7], 21
n = len(val)

items = [[val[i],wt[i]] for i in range(n)]
items.sort(key=lambda x:x[0]/x[1],reverse=True)
total_value = 0
for i in range(n):
    if items[i][1]<=capacity:
        total_value+=items[i][0]
        capacity-=items[i][1]
    else:
        fraction = capacity/items[i][1]
        total_value+=(items[i][0]*fraction)
        break
print(float(f"{total_value:.6f}"))       
