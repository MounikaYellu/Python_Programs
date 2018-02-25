# hanoi.py
# recursive solution to towers of hanoi problem .
def moveTower(n,source,dest,temp):
	if n==1:
		print("Move disk from {0} to {1} .").format(source,dest)
	else:
		moveTower(n-1,source,temp,dest)
		moveTower(1,source,dest,temp)
		moveTower(n-1,temp,dest,source)
def hanoi(n):
	moveTower(n,"A","C","B")
def main():
	print("Towers of Hanoi")
	n=int(input("How many disks?"))
	hanoi(n)
if __name__=='__main__': main()
