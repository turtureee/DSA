digits = list(map (int, input()))

if digits[len(digits)-1]==9:
    digits[len(digits)-1]+=1
    for i in range(len(digits)-1,0,-1):
        if digits[i]==10:
            digits[i]=0
            digits[i-1]+=1
else:
    digits[len(digits)-1]+=1

if digits[0]==10:
    digits.remove(10)
    digits.insert(0,1)
    digits.insert(1,0)
print(digits)
        
