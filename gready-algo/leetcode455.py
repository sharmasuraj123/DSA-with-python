players, trainers = [4, 7, 9], [8, 2, 5, 8]
trainers.sort()
players.sort()
count,j = 0,0
for i in range(0, len(players)):
    while j < len(trainers):
        if trainers[j] >= players[i]:
            count+=1
            j+=1
            break
        j+=1
print(count)        
