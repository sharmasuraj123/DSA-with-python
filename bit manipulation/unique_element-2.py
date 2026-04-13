from collections import defaultdict
arr = [1,1,2,2,3,3,4,5]
Map = defaultdict(int)
ele = []
for i in arr:
    Map[i]+=1
for key,value in Map.items():
    if value<2:
        ele.append(key)
if len(ele) >= 2 and ele[0] > ele[1]:
    ele[0],ele[1] = ele[1],ele[0]
print(ele)   



