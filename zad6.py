import random
def gen_number():
	number='0444'
	d=0
	for i in range(0,999):
		d=len(number)
		if d<11:
			c=random.randrange(0,9)
			if (c==1) or (c==4) or( c== 5) or (c==7) or (c==9)  or (c==0):
				f=str(c)
				number=number+f
			else:
				continue
	print("new number: ", number)
gen_number()
