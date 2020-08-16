def insertList(list, start, end, mid, value):
	pos=-1
	while start<=end:
		pos = start if start==end and value<=list[start] else start+1
		if start+1==end:
			if list[end]<=value:
				pos=end+1
			elif list[start]<value and list[end]>value:
				pos=end
			elif list[start]>=value:
				pos=start
			break			
		elif list[mid]==value:
			pos=mid
			break
		elif list[mid]<value:
			start=mid+1
			mid=(start+end)//2
		elif list[mid]>value:
			end=mid-1
			mid=(start+end)//2
	list.insert(pos,value)
		
def getMedian(median, is_odd_len):
	if is_odd_len==True:
		return median;
	else:
		return median+1;
		
inp = [0,82,180,55,168,41,179,59,139,71,6,12,135,139,73,157,4,74,195,60,45,28,67,136,58,55,22,60,33]
in_sort_list = []
is_odd_len = False;
median = -1
for val in inp:
	if len(in_sort_list)==0:
		in_sort_list = [val]
		is_odd_len = True
		median = 0
	else:
		insertList(in_sort_list, 0, len(in_sort_list)-1, median, val)
		median=getMedian(median, is_odd_len);
		is_odd_len = not is_odd_len
print (in_sort_list, median)