from re import X


allnumber = int(input("how many numbers do yo have for calculation :  "))
y2 = []
for i in range(1,allnumber+1):
    
    x = int(input(f"enter your number {i} : "))
    y2.append(x)
    
# sum
total = 0
for i in range(0,len(y2)):
    total = total + y2[i]
print(f"your sum is : {total}")

# muntiply
totalmun = 1
for i in range(0,len(y2)):
    totalmun = (totalmun)*(y2[i])
print("************** Your sum and muntiplz is here ***********" "\n")
print(f"your sum is : {total}""\n")
print(f"your muntiply  is : {totalmun}""\n")
print("************** Thank You ***********" "\n")