prices = [7,6,4,3,1]

buy,sell,profit = 0,0,0
for i in range(len(prices)):
    if prices[i]<prices[buy]:
        buy = i
        sell = i
    else:
        sell = i
        profit = max(profit,prices[sell]-prices[buy])
print(profit)            