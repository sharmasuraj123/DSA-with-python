s = "rat"
t = "car"
arr = [0]*26
for i in range(len(s)):
    arr[ord(s[i]) - ord("a")]+=1
for i in range(len(t)):
    arr[ord(t[i]) - ord("a")] -= 1
for i in arr:
    if i!=0:
        print(False)
        break
print(True)
