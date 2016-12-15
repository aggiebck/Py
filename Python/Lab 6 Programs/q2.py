import random

def blackjack():
        play = 1
        while (play == 1):
                print("Welcome to Black Jack")
                input("Press enter to roll...")

                ply_die1 = random.randrange(1, 11)
                ply_die2 = random.randrange(1, 11)

                comp_die1 = random.randrange(1, 11)
                comp_die2 = random.randrange(1, 11)

                ply_total = ply_die1 + ply_die2
                comp_total = comp_die1 + comp_die2

                print("You rolled a", ply_die1, "and", ply_die2, "Totaling", ply_total)
                roll_again = input("would you like to roll again? ")


                if (roll_again == 'y' or roll_again == 'Y'):
                        ply_dieagain = random.randrange(1, 11)
                        ply_total = ply_total + ply_dieagain
                        
                if (comp_total < 16):
                        comp_dieagain = random.randrange(1, 11)
                        comp_total = comp_total + comp_dieagain
                print("You rolled a total of ", ply_total)
                print("The computer rolled a total of ", comp_total)

                if (ply_total > 21):
                        print ("Oops, looks like you busted")
                elif (comp_total > 21):
                        print("Oops looks like the computer busted, You win!!")
                elif (ply_total > comp_total):
                        print("Yay, you won!!")
                elif (comp_total > ply_total):
                        print("Damn the computer won")
                play_input = input("Play again y or n")
                if (play_input == 'y' or play_input == 'Y'):
                        play = 1
                else:
                        play = 0
                        
                        
blackjack()
