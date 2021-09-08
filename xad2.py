#zadanie 2
'''
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
import random
x=[]
for i in range(4):
	x.append(random.choice(names))
print(x)
'''
#zadanie6

names =["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
import random
first=[]
second=[]
third=[]
last=[]
for i in range(1,4):
	c=random.choice(names)
	first.append(c)
	names.remove(c)
for i in range(1,4):
	c=random.choice(names)
	second.append(c)
	names.remove(c)
for i in range(1,4):
	c=random.choice(names)
	third.append(c)
	names.remove(c)
last.append(names)
print("first team: ", first)
print("2: ", second)
print("3", third)
print(last)
