print("Getting the magic numbers...")
n,k,c=99999,0,0
while(k<=n):
	t=int(round(k**(1/3),5))
	flag=0
	store=-1
	for first in range(1,t):
		i=first**3
		temp_second = round((k-i)**(1/3),5)
		second = int(temp_second)
		if (temp_second==second):
			if (flag==0):
				flag+=1
				store = first
				pair = {(first,second)}
			elif(flag!=0 and ((first,second) not in pair) and ((second,first) not in pair)):
				flag+=1
				pair.add((first,second))
				break;
	if flag>=2:
		print("Magic No",c,": ")
		print(pair)
		print("Result",	 k)
		print("\n")
		c+=1
	k+=1