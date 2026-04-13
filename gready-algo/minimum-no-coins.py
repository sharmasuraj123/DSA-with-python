n = 39
notes = [10,5,2,1]
count = 0
for i in notes:
    if n//i>0:
        count+=(n//i)
        n%=i
print(-1 if n else count)                
                    
       