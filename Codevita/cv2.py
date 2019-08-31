room = int(input())
r1,r2 = [int(x) for x in input().split()]
rev = int(input())
patient = []
for i in (1,3,5,7,8,10,12):
    for j in range(1,32):
        patient.append(((6-i)**2)+abs(j-15))
for i in (4,6,9,11):
    for j in range(1,31):
        patient.append(((6-i)**2)+abs(j-15))
for j in range(1,29):
    patient.append(16+abs(j-15))
tv = 0
flag = False
for i in range(0,room+1):
    sum = 0
    for j in patient:
        if j>room:
            sum += r1*i+r2*(room-i)
        else:
            if j>room-i:
                sum += (room-i)*r2+(j-(room-i))*r1
            else:
                sum += j*r2
    if sum>rev:
        flag = True
        tv = i
        break
if flag==True:
    print (tv)
else:
    print (room)
