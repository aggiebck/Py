from random import*
def rolldice():
    global r3 #This is a constant within the function
    #r=0#---
    #r=1#----
    #r=2#----- Tests for
    #r=3#----- different answers
    #r=4#----
    #r=5#---    
    r=randrange(6)
    r2=randrange(6)
    r3=((r+1)+(r2+1)) #The constant global variable
    C=('* ')
    s=('+-------+\n|'+C[r<1]+'     '+C[r<3]+'|\n|  '+C[r<5])
    s2=('+-------+\n|'+C[r2<1]+'     '+C[r2<3]+'|\n|  '+C[r2<5])
    #print (r)
    #print (r2)
    #print (r3)
    #print (s[::-1])
    #print ()
    #print ()
    #print (s+C[r&1])
    #print ()
    #print ()
    '''list_a = ['+-------+','|'+C[r<1]+'     '+C[r<3]+'|','  '+C[r<5],s[::-1]]
    list_b = ['+-------+','|'+C[r2<1]+'     '+C[r2<3]+'|','  '+C[r2<5]]
    counter = 0
    while counter < 5:
        print (list_a[counter])
        counter += 1'''
        
    a = (s+C[r&1]+s[::-1])
    b = (s2+C[r2&1]+s2[::-1])
    print(a)
    print(b)
    #print (a,b)
    
    return (r3)

def main():
    print('Craps : A Popular Dice Game')
    input('Press <Enter> to roll the dice .')
    rolldice()
    o_r3 = r3
    #print (o_r3)
    if r3 == 7:
        print('You rolled a',r3,'on your first roll.')
        print('You Win!')
        print()
        main()
    elif r3 == 3:
        print('You rolled a',r3,'on your first roll.')
        print('You Lose!')
        print()
        main()
    else:
        print('You rolled a',r3,'on your first roll.')
        print()
        print('That’s your point . Roll it again before you roll 7 and Win !')
        print()       
    while r3 != 7 or r3 != o_r3:
        #print(r3)
        #print(o_r3)        
        input('Press <Enter> to roll the dice .')
        print()
        rolldice()
        print('You rolled a',r3,'.')
        if r3 == 7:
            print('You Lose!')
            print()
            main()
        if r3 == o_r3:
            print('You Win!')
            print()
            main()        

main()
    
    




