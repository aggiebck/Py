# A program to play Blackjack Dice. 

import random

def roll_die():
    random_die = random.randint(1, 11)
    return random_die

def player():
    global r1
    global r2
    global ply_total
    r1 = roll_die()
    r2 = roll_die()
    blackjack = False
    ply_total = 0    
    print('************ YOUR TURN ************')
    print("Roll: ", r1, r2)
    ply_total = r1 + r2
    if ply_total == 21:
        blackjack = True
        print("Blackjack!") 
        print()
        print('************ GAME OVER ************')
        print("You win!") 
        restart()
    print("Total: ", ply_total)
    reroll = (input("(s)tay or (r)oll? "))
    print()
    while ply_total > 0:
        if reroll ==  "r" or reroll == "R":
            r1=roll_die()
            print("Roll: ", r1)
            ply_total = ply_total + r1
            print("Total: ", ply_total)
            print()
            if  ply_total >= 22:
                print("Bust!")
                print('************ GAME OVER ************')
                print("Dealer Wins!")
                restart()
            elif ply_total == 21:
                blackjack = True
                print("Blackjack!") 
                print()
                print('************ GAME OVER ************')
                print("You win!") 
                restart()
            reroll = (input("(s)tay or (r)oll? "))              
        elif reroll == "s" or reroll == "S":
            dealer()
        else:
            print("Sorry Please Try again")
            print()
            player()       
    return ply_total, blackjack 

def dealer():
    print("\n********** DEALER'S TURN **********")
    comp_total = 0
    print("Roll: ", r1, r2)
    comp_total = r1 + r2
    print("Total: ", comp_total)   
    while comp_total <= 17:
        print(input("Press Enter to Continue ..."))
        print("Roll: ", r1)
        comp_total = comp_total + r1
        print("Total: ", comp_total)      
        if comp_total >= 22:
            print("Bust!")
            print('************ GAME OVER ************')
            print("You Wins!")
            restart()            
        elif comp_total == 21:
            print("Blackjack!") 
            print()
            print('************ GAME OVER ************')
            print("Dealer Wins!") 
            restart()
        if comp_total > ply_total:
            print('************ GAME OVER ************')
            print("Dealer Wins!")
            restart()
   
def restart():
    restart = (input("Would you like to play again -- (y) or (n)?"))
    if restart == "y" or restart == "Y":
        main()
    else: 
        quit()

def main():
    
    # The user (or player) plays first.
    ply_total, blackjack = player()
     

    
    
    
main()