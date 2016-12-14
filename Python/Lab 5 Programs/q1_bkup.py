# A Python program for the Rock, Paper, Scissors game. 
import random

def rock_paper_scissors():
    pl_score = 0
    comp_score = 0
    comp_possible = 1,2,3
    game_stop = True
    while game_stop == True:
        comp_choice = random.choice(comp_possible)        
        print()
        pl_input = ((input("Pick your throw: [r]ock, [p]aper, [s]cissors, or [q]uit? ")))
       
        choice = pl_input
        if choice == "r" or choice == "R":
            pl_choice = 1
        elif choice == "s" or choice == "S":
            pl_choice = 2
        elif choice == "p" or choice == "P":
            pl_choice = 3
        elif choice == "q" or game_stop == "Q":
        	quit()
        else:
            print ("That was not a valid choice.")
            print ("Please Try again")
            rock_paper_scissors()        
        if comp_choice == 1:
            comp_string = ("Rock")
        elif comp_choice == 2:
            comp_string = ("Scissors")
        else:
            comp_string = ("Paper")
        if pl_choice == comp_choice:
            print ("Tie!")
        elif (pl_choice == 1 and comp_choice == 2) or (pl_choice == 2 and comp_choice == 3) or (pl_choice == 3 and comp_choice == 1):
            print("Computer threw",comp_string,"you win!")
            pl_score+=1
        else:
            print("Computer threw",comp_string,"you lose!")
            comp_score+=1
        print("Your Score: ", pl_score)
        print("Computer Score: ", comp_score)
        
        

def main():
    print('ROCK PAPER SCISSORS in Python')
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock.')  
    rounds_possible = 1,2,3
    rounds_rand = random.choice(rounds_possible)
    round_count = 1
    count = rounds_rand 
    star = "*"      
    print()
    print("How Many Points does it take to win?", count)
    print()
    if count > 0:
        print(star*21, "ROUND", "#",round_count, star*21)
        round_count+=1          
    rock_paper_scissors()
main()