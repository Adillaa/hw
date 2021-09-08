def fibo(num):
	a=1
	b=1
	ans=[]
	ans.append(0)
	ans.append(1)
	for i in range(0,num):
		c=len(ans)
		if c== num:
			break
		b=a+b
		ans.append(a)
		ans.append(b)
		a=b+a
	print(ans)
fibo(10)
