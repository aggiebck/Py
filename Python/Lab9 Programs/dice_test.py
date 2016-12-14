from random import*
#r=randrange(6)
#r=0
#r=1
#r=2
#r=3
#r=4
r=5
C=('o ')
s=('+-------+\n|'+C[r<1]+'     '+C[r<3]+'|\n|  '+C[r<5])
print (r)
print (s[::-1])
print ()
print ()
print (s+C[r&1])
print ()
print ()
a = (s+C[r&1]+s[::-1])
print (a)