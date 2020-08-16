arr=[1,3,8,9,11]
i,j,diff,x,y=0,0,9999999999,-1,-1
while(i<len(arr) and j<len(arr)):
	if(i!=j and diff>abs(arr[i]-arr[j])):
		diff=abs(arr[i]-arr[j])
		x=arr[i]
		y=arr[j]
	if(arr[i]>arr[j]):
		j+=1
	else:
		i+=1
print("Closest Diff:",diff)
print("Elements Are: " ,x, y)
