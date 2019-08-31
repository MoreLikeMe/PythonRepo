import math
n1,n2 = [int(x) for x in input().split()]
prime = []
for i in range(n1,n2+1):
    flag = True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag = False
            break
    if flag == True:
        prime.append(i)
if prime[0] == 1:
    prime = prime[1:]
uniqCombList = []
for i in range(len(prime)):
    for j in range(len(prime)):
        if i!=j and int(str(prime[i])+str(prime[j])) not in uniqCombList:
            uniqCombList.append(int(str(prime[i])+str(prime[j])))

uniqPrimeList = []
for i in uniqCombList:
    flag = True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag = False
            break
    if flag == True:
        uniqPrimeList.append(i)
l = len(uniqPrimeList)
min = min(uniqPrimeList)
max = max(uniqPrimeList)
count = 2
while(count<l):
    c = min + max
    min = max
    max = c
    count+=1
print (max)
