n = input("Enter the length of fibonacci series: ")
try:
	n = int(n)
	a,b = 0,1
	while(n):
		print(a+b, end=" ")
		a,b = b,a+b
		n=n-1
except ValueError:
	print("Not a Valid Input")