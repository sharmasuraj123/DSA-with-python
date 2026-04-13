num = "4206"
i = len(num)-1

while i>=0:
    if num[i]%2!=0:
        print(num[:i+1])
        break
    else:
        i-=1
        