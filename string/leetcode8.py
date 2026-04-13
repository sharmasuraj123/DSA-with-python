s = "-91283472332"
pOrn = "+"
new_s = s.strip()
MaxNegative = -(2**31)
MaxPossitive = 2**31 - 1
print(MaxNegative,MaxPossitive)
Value = 0
if new_s[0]=="+" or new_s[0]=="-":
    pOrn = new_s[0]
for i in range(len(new_s)):
    aciii = ord(new_s[i])
    if 48 <= (aciii) <= 57:
        Value = Value * 10 + (aciii-ord("0"))
    else:
        if ((i>0) or (new_s[0]!="+" and new_s[0]!="-")):break
            
print(Value)        
if pOrn == "-":
    if -1*Value < MaxNegative:
        print(MaxNegative)
    else:
        print(-1 * Value)
else:
    if Value > MaxPossitive:
        print(MaxPossitive)
    else:
        print(Value)
