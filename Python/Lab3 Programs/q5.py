#Variables

n1 = float(input("Number #1: "))
n2 = float(input("Number #2: "))
n3 = float(input("Number #3: "))

#Check for different permutations

if n2>n3 and n1>n3:
    if n1>n2:
        print("Sorted Order: ", n3, n2, n1)
    if n2>n1:
        print ("Sorted Order: ", n3, n1, n2)
if n1>n2 and n3>n2:
    if n3>n1:
        print ("Sorted Order: ", n2, n1, n3)
        if n1>n3:
            print ("Sorted Order: ", n2, n3, n1)
if n2>n1 and n3>n1:
    if n3>n2:
        print ("Sorted Order: ", n1, n2, n3)
        if n2>n3:
            print ("Sorted Order: ", n1, n3, n2)
            
#Final check for equal numbers

if n1 == n2:
    if n1>n3:
        print("Sorted Order: ", n3,n2,n1)
    if n3>n1:
        print("Sorted Order: ", n1,n2,n3)
if n1 == n3:
    if n1>n2:
        print ("Sorted Order: ", n2,n1,n3)
    if n2>n1:
        print ("Sorted Order: ", n1,n3,n2)
if n2 == n3: 
    if n1>n2:
        print ("Sorted Order: ", n3,n2,n1)
    if n2>n1:
        print ("Sorted Order: ", n1,n2,n3)
