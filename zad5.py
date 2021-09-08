import webbrowser
def create(name):
	webbrowser.open('/home/adilla/Python/practice/function')
	with open(name,"w") as f:
		f.write("new file is ready to use")
create("nachalo")
