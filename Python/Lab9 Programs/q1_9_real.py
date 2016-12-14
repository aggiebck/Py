
def addition():
    stop = 0
    n1 = (int(input("Number #1: ")))
    n2 = (int(input("Number #2: ")))
    l = len(str(n1))
    l1 = len(str(n2))
    l2 = str(n1*n2)
    print()
    if n1 or n2 > 0:
        if l > l1:
            l2 = str(n1*n2)
            print(" "*(len(l2)-l-1),max(n1,n2))
        else:
            print(" "*(len(l2)-l1-1),max(n1,n2))
        print("x")
        if l > l1:
            print(" "*(len(l2)-l-1),min(n1,n2))
        else:
            print(" "*(len(l2)-l1-1),min(n1,n2))
        print('-'*(len(l2)))
        print(n1*n2)
        
        stop+=1
    else: 
        print ("The Answer is: 0")
        addition()

def number_of_carries():
    num1 = str(n1)
    num2 = str(n2)
    carry = 0
    carries = 0
    c1 = l
    c2 = l
    if (l < l1):
        while (c1 < l1):
            num1 = '0' + num1
            c1+=1
    if (l1 < l):
        while (c2 < l):
            num2 = '0' + num2
            c2+=1
    i = c1
    while (i > 0):
        if (int(num1[i-1])+int(num2[i-1])+carry > 9):
            carry = 1;
            carries+=1
        else:
            carry = 0
        i-=1
    return carries
        
addition()

print()
print('Carries : ',number_of_carries())