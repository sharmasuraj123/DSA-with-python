cardPoints = [1,2,3,4,5,6,1]
k = 3
n = len(cardPoints)
w_sum,total = 0,sum(cardPoints)
for i in range(n-k):
    w_sum+=cardPoints[i]
max_sum = total-w_sum
w_s,w_e = 0,n-k
while w_e<n:
    w_sum+=cardPoints[w_e]
    w_sum-=cardPoints[w_s]
    max_sum = max(max_sum,total-w_sum)
    w_e+=1
    w_s+=1
print(max_sum) 