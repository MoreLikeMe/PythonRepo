arr1=[1,3,8,9,11]
arr2=[5,7,14,17]
i,j,diff,x,y=0,0,9999999999,-1,-1
while(i<len(arr1) and j<len(arr2)):
	if(diff>abs(arr1[i]-arr2[j])):
		diff=abs(arr1[i]-arr2[j])
		x=arr1[i]
		y=arr2[j]
	if(arr1[i]>arr2[j]):
		j+=1
	else:
		i+=1
print("Closest Diff:",diff)
print("Elements Are: " ,x, y)
