def modulator():
	count = 0
	if count == 0:
		n1 = (float(input("Enter Number 1:")))
		n2 = (float(input("Enter Number 2:")))
		nmod1 = n1%100
		nmod2 = n2%100
		sum = ((n1%100) + (n2%100))
		print(nmod1)
		print(nmod2)
		print(sum)
		count+=1
	
modulator()