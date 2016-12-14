s = int(input("Starting Year: "))
e = int(input("Ending Year: "))
print()

while True:
    if s > e:
        print( s, "is >", e, "the starting year must be larger than the ending year, please try again")
    break

if s <= e:
    print("Leap Years Between", s, "and", e) 
    
while s <= e:    
    if s%4==0 and s%100!=0:
        print(s)
    if s%100==0 and s%400==0:
        print(s)   
    s+=1