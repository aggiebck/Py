a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
e = float(input("Enter e: "))
f = float(input("Enter f: "))

print()
print ("Solving for the following two equations")
print (str(a)+"x +", str(b)+"y =", str(e))
print (str(c)+"x +", str(d)+"y =", str(f))
print()

if (a * d) - (b * c) == 0:
    print ("No Solution Found")
else:
    x = ((e * d - b * f) / (a * d - b * c)) 
    y = ((a * f - e * c) / (a * d - b * c))
    print ("x =", x) 
    print ("y =", y)  

   


