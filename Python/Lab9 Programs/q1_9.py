def multi(n1, n2):
    n1str = str(n1)
    n2str = str(n2)
    l = len(n1str)
    l1 = len(n2str)
    answer = []
    carrycount = 0
    carrylist = [0,0,0,0,0,0,0,0,0,0]
    if n1 < n2:
        for i in n1str[::-1]:
            int_i = int(i)
            n3 = (n2*int_i)
            #print(int_i)
            #print(n3) #Test
            answer.append(n3)  
    else:
        for i in n2str[::-1]:
            int_i = int(i)
            n3 = (n1*int_i)
            #print(int_i)
            #print(n3) #Test
            answer.append(n3)            
    a_enum = list(enumerate(answer,1))
    #print(a_enum) #Test
    #print (l, l1) #Test
    for a in range(0,len(str(n1))):
        n1str[-a]
        for b in range(0,len(str(n2))):
                    temproduct = (int(n2str[-b])*int(n1str[-a]))
                    if temproduct > 9:
                        tempcarry = temproduct//10
                        carrylist[tempcarry] = carrylist[tempcarry]+1
                        carrycount += 1     

    if l == 1 or l1 == 1:
        if n1 and n2 != 0:
            l2 = str(n1*n2)
            if l > l1:
                print(""*(len(l2)-l),max(n1,n2))
                #print(1)
            else:
                print(""*(len(l2)-l1),max(n1,n2))
                #print(2)
            if l > l1:
                print("x",""*(len(l2)-l),min(n1,n2))
                print("-"*(len(l2)))
                print(n1*n2)
                #print(3)
            else:
                print("x",""*(len(l2)-l1),min(n1,n2))
                print("-"*(len(l2)))
                print(n1*n2)
                #print(4)
        else:
            if l > l1:
                print(" ",max(n1,n2))
                print("x","  ",min(n1,n2))
                print("------")
                print(" "*4,(answer[0]))                
                #print(1)
            else:
                print(" ",max(n1,n2))
                print("x","  ",min(n1,n2))
                print("------")
                print(" "*4,answer[0])
                #print(2)
    elif l == 2 or l1 == 2:
        l2 = str(answer[0])
        l3 = str(n1*n2)
        if l > l1:
            print(" "*(len(l3)-l+2),max(n1,n2))
            #print(len(l3)-l)
            #print(1)
        else:  
            print(" "*(len(l3)-l1+2),max(n1,n2))
            #print(2)
        if l > l1:
            print("   x"," "*(len(l3)-l-1),min(n1,n2))
            print("  ","-"*(len(l2)+2))
            print(" "*(len(l2)-2),answer[0])
            #print(3)
        else:
            print("   x"," "*(len(l3)-l1-1),min(n1,n2))
            print("  ","-"*(len(l2)))
            print(" "*(len(l2)),answer[0])
            #print(4)
        pos = 1
        #print(len(answer)-1)
        for i in range(1,(len(answer))):
            if pos != (len(answer)-1):
                print(" "*(len(l2)-5),answer[pos])
                pos += 1
                #print('a')
            else:
                print("+"," "*(len(l2)-6),answer[pos])
                print("-"*(len(l3)+3))
                print(" "*(len(l3)-4),n1*n2)
                #print('b')
        print()
        print("Total Carries: ",carrycount)
        print()
        print("Carry digit --> Frequency")
        print()
        for number, count in enumerate(carrylist,0):
            print(number, "-->", count)              
                
    elif l == 3 or l1 == 3:
        l2 = str(answer[0])
        l3 = str(n1*n2)
        l4 = (len(answer)-1+len(str(answer[-1]))+2)
        #print(answer)
        #print(l4)
        if l > l1:
            print(" "*(len(l3)-l+1),max(n1,n2))
            #print(len(l3)-l)
            #print(1)
        else:  
            print(" "*(len(l3)-l1+1),max(n1,n2))
            #print(2)
        if l > l1:
            print("   x"," "*(len(l3)-l+2),min(n1,n2))
            print(" ","-"*(len(l2)+2))
            #print(" ",answer[0])
            #print(3)
        else:
            print("   x"," "*(len(l3)-l1+2),min(n1,n2))
            print(" ","-"*(len(l2)+2))
            #print(" ",answer[0])
            #print(4)
        pos = 0
        subtract = 0
        #print(len(answer)-1)
        for i in range(0,(len(answer))):
            #print(pos)
            if pos != (len(answer)-1):
                print("  "+" "*(l4-subtract-len(str(answer[pos]))-2)+str(answer[pos]))
                pos += 1
                subtract += 1
                #print('a')
            else:
                print("+",answer[pos])
                print("-"*(len(l3)+1))
                print(""*(len(l3)-5),n1*n2)  
                #print('b')
        print()        
        print("Total Carries: ",carrycount)
        print()
        print("Carry digit --> Frequency")
        print()
        for number, count in enumerate(carrylist,0):
            print(number, "-->", count)                
    else:
        l2 = str(answer[0])
        l3 = str(n1*n2)
        l4 = (len(answer)-1+len(str(answer[-1]))+2)
        #print(answer)
        #print(l4)
        if l >= l1:
            print(" "*(len(l3)-l+1),max(n1,n2))
            #print(len(l3)-l)
            #print(1)
        else:  
            print(" "*(len(l3)-l1),max(n1,n2))
            #print(2)
        if l >= l1:
            print(" "*(len(l3)-l),"x",min(n1,n2))
            print("  "*(len(l3)-l-6),"-"*(len(l2)+3))
            #print(" ",answer[0])
            #print(3)
        else:
            print(" "*(len(l3)-l1),"x",min(n1,n2))
            print("  "*(len(l3)-l1-6),"-"*(len(l2)+3))
            #print(" ",answer[0])
            #print(4)
        pos = 0
        subtract = 0
        #print(len(answer)-1)
        for i in range(0,(len(answer))):
            #print(pos)
            if pos != (len(answer)-1):
                print("  "+" "*(l4-subtract-len(str(answer[pos]))-2)+str(answer[pos]))
                pos += 1
                subtract += 1
                #print('a')
            else:
                print("+",answer[pos])
                print("-"*(len(l3)+1))
                print(""*(len(l3)-5),n1*n2)  
                #print('b')
        print()        
        print("Total Carries: ",carrycount)
        print()
        print("Carry digit --> Frequency")
        print()
        for number, count in enumerate(carrylist,0):
            print(number, "-->", count) 
        

def main():
    n1 = (int(input("Number #1: ")))
    n2 = (int(input("Number #2: ")))
    while n1 or n2 != 'quit':
        multi(n1,n2)
        print()
        n1 = (int(input("Number #1: ")))
        n2 = (int(input("Number #2: ")))                
main()