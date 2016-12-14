import random

def welcome():
    print('-----------------------------')
    print( '| Welcome to Cows and Bulls |')
    print( '-----------------------------')
    


def main():
    welcome()
    comp_guess = str(random.randint(100,999))
    g_list = []
    cows = 0
    for g in comp_guess:
        g_list.append(g)    
    check = False
    while check == False:
        if g_list[0] in g_list[1] or g_list[0] in g_list[2] or g_list[1] in g_list[2]:
            comp_guess = str(random.randint(100,999))
            g_list = comp_guess
        else:
            check = True   
    count = 0
    '''print(comp_guess)''' #check the answer
    while cows < 4 and exit !="x":
        count+=1
        user_guess = input("Guess #"+ str(count)+ ": ")
        g2_list = []
        cows = 0
        bulls = 0
        if user_guess != "x":
            for i in user_guess:
                g2_list.append(i)
            '''print(g_list, g2_list)''' # for troublshooting the lists
            for i in range(0,3):
                if g_list[i] == g2_list[i]:
                    cows +=1
            if g_list[0] in g2_list[1] or g_list[0] in g2_list[2]:
                bulls += 1
            if g_list[1] in g2_list[0] or g_list[1] in g2_list[2]:
                bulls += 1
            if g_list[2] in g2_list[1] or g_list[2] in g2_list[0]:
                bulls += 1            
            print(cows, "cows", bulls, "bulls")
            if cows == 3 and g_list[0] == g2_list[0] and g_list[1] == g2_list[1] and g_list[2] == g2_list[2]:
                print()
                print("You Got it!")
                print("It took you",count,"guesses to guess the secret number", comp_guess)
                print()
                main()
            
main()