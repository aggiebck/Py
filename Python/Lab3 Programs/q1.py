change = float(input("Enter the change amount: "))

p = int(change * 100)
d1= (p // 100)
change2 = (p%100)
q = (change2//25)
change3 = (change2%25)
d = (change3//10)
change4 = (change3%10)
n = (change4//5)
change5 = (change4%5)
p2 = (change5//1)

print (d1, "Dollars", "\n", q, "Quarters", "\n", d, "Dimes", "\n", n, "Nickles", "\n", p2, "Pennies", "\n")

