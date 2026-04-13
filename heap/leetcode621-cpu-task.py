import heapq
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
hashMap = {}
for i in tasks:
    hashMap[i] = hashMap.get(i,0)+1
pq,q,time = [],[],0
for idx,val in hashMap.items():
    heapq.heappush(pq,-val)   
while pq or q:
    time+=1
    if pq:
        x = heapq.heappop(pq)
        x+=1
        if x<0:
            q.append((x,time+n))
    if len(q) and  q[0][1]<=time:
        heapq.heappush(pq,q[0][0])
        q.pop(0)
print(time)
