def generator():
	for i in range(6):
		yield i*i
g=generator()
print dir(g)
for i in g:
	print(i)
