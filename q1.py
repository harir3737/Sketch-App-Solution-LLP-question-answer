def findindex(x,y):
		cont=x.count(y)
		if cont==1:
			for i in x:
				if i==y:
					ind=x.index(i)
					print(ind)
		elif(cont==0):
			print("\nindex 5 is the only possible place to insert",y)
				
a=[1,2,4,5,6]
p=int(input("enter a number\t"))
findindex(a,p)