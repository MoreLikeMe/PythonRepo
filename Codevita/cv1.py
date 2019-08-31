n = [x for x in input().split()]
min = 9999999999999999
for i in n:
    max = -1
    for j in range(len(i)):
        if ord(i[j])>=65:
            val = ord(i[j])-55
        else:
            val = int(i[j])
        if val>max:
            max = val
    sum = 0
    for k in range(len(i)):
        if ord(i[-(k+1)])>=65:
            v = ord(i[-(k+1)])-55
        else:
            v = int(i[-(k+1)])
        sum += v*((max+1)**(k))
    if sum<min:
        min = sum
print (min)
