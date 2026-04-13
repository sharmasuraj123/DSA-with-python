import math
N = 16
divisor = []
for i in range(1,int(math.sqrt(N))+1):
    if N%i==0:
        if N//i==i:
            print(i, end=" ")
        else:
            print(i,end=" ")
            divisor.append(N//i)               
for i in range(len(divisor) - 1, -1, -1):
    print(divisor[i], end=" ")
