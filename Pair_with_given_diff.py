#
#
##NotWorkable Code
#
#
def closestPair(arr,i,j,diff):
	if(i<0 or j<0 or i>=len(arr) or j>=len(arr)):
		return
	if(abs(arr[j]-arr[i])==diff):
		print(arr[j],arr[i])
		return
	closestPair(arr,i,j+1,diff)
	closestPair(arr,i-1,j,diff)
	closestPair(arr,i-1,j+1,diff)

arr=[3,9,8,11,1,80,75]
closestPair(arr,len(arr)//2,len(arr)//2,1)