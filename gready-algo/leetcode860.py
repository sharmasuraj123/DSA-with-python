bills = [5, 5, 10, 10, 20]
collection = {}
for i in bills:
    if i==10:
        x = collection.get("5",0)
        if x<1:
            print(False)
            break
        else:
            collection["5"] = collection.get("5",0)-1
            collection["10"] = collection.get("10",0)+1
    elif i == 20:
        x = collection.get("5",0) 
        y = collection.get("10",0)
        if x>0 and y>0:
            collection["10"] = collection["10"]-1
            collection["5"] = collection["5"] - 1
            collection["20"] = collection.get("20",0)+1
        else:
            print(False)
            break
    else:
        collection["5"] = collection.get("5",0) + 1
print(True)        
