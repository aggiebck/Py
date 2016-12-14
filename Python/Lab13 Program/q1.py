import random


def check_bingo(card):
    ''' Checks whether card has Bingo. 
        
        Keyword argument:
        
            card: a dictionary where the keys are the 
                  strings 'B', 'I', 'N', 'G', and 'O'.
                  The values for each key is a list of
                  five integers, where the values for
                  the key 'B' are in the range 1 to 15,
                  the values for key 'I' are in the range
                  16 to 30, etc.
                    
                  The integer 0 is used to represent a value 
                  that has been called.
                
        Returns:
            True if the dictionary structure card contains Bingo.
            Otherwise, returns False.
            
                    
        Example: 
        
            Suppose card = {'B':[1,4,8,11,12], 'I':[19,0,26,0,0],
                            'N':[0,35,0,41,42], 'G':[49,51,0,56,58],
                            'O':[0,69,71,73,74]}.
            Then, this function would return False.
    '''
    
    # enter your code here.
    #opprint(card)
    
    #Diagonals ~~~
    #print('1')
    d1check = False
    for i in ('B0','I1','G3','O4'):
        tempcheck = True
        if card[i[0]][int(i[1])] != 0:
            tempcheck = False
    if tempcheck == True:
        d1check = True
        return d1check
    else: pass
    
    d2check = False
    for i in ('O0','G1','I3','B4'):
        tempcheck = True
        if card[i[0]][int(i[1])] != 0:
            tempcheck = False
    if tempcheck == True:
        d2check = True
        return d2check
    else:
        pass
        
    #Columns ~~~
    #print('2')
    if sum(card['B']) == 0:
        return True
    elif sum(card['I']) == 0:
        return True
    elif sum(card['N']) == 0:
        return True
    elif sum(card['G']) == 0:
        return True
    elif sum(card['O']) == 0:
        return True
    else:
        pass
    
    #Rows ~~~
    #print('3')
    check = False
    for i in range(0,5):
        tempcheck = True
        for l in 'B','I','N','G','O':
            #print(card[l][i])
            if card[l][i] != 0:
                tempcheck = False
        if tempcheck == True:
            check = True
    return check


def generate_random_card():
    ''' Generates a random Bingo card.  
    
        Keyword arguments: None
        
        Returns:
            a dictionary that represents a valid Bingo card.
            
            Remember, a valid Bingo card is a dictionary where 
            the keys are the strings 'B', 'I', 'N', 'G', and 'O'.
            The values for each key is a list of five integers, where 
            the values for the key 'B' are in the range 1 to 15,
            the values for key 'I' are in the range 16 to 30, etc.
    '''   
    
    # card is a dictionary that will hold a random card.  You can call
    # this variable whatever you like.  Just make sure you change
    # the return statement if you do change the variable name.
    card = {}
    
    Blist = (random.sample(range(1,16),5))
    card['B'] = Blist
    #print(Blist)
    Ilist = (random.sample(range(16,31),5))
    card['I'] = Ilist
    #print(Ilist)
    Nlist = (random.sample(range(31,46),5))
    Nlist[2] = 0
    card['N'] = Nlist
    #print(Nlist)
    Glist = (random.sample(range(46,61),5))
    card['G'] = Glist
    #print(Glist)
    Olist = (random.sample(range(61,76),5))
    card['O'] = Olist
    #print(Olist)
    #print(card)
    
    return card


def simulate_bingo(n, k):
    ''' Simulates k trials of Bingo, where n cards are 
        in play during the simulation.
    
        Keyword arguments:
        
           n: the number of cards in play during a game of Bingo 
           
           k: the total number of games (trials) to play
           
        Returns:
            3 floating point values (minn, maxx, avg) returned.
            
            minn: the minimum number of calls
                required to get Bingo among the k games of
                Bingo played with n cards.
            
            maxx: maximum number of Bingo calls.
            
            avg: average number of Bingo calls.
            
    '''  
    n = int(n)
    k = int(k)

    minn = 0
    maxx = 0
    avg = 0
    
    # enter your code here
    x = 1
    countlist= []
    while x<=k:
        boardlist=[]
        for i in range(0,n):
            var=generate_random_card()
            boardlist.append(var)
        #print(boardlist)
        bingo=False
        y = 0
        while bingo==False:
            number=random.randint(0,75)
            for i in boardlist:
                for a in range(0,4):
                    if i['B'][a]==number:
                        i['B'][a]=0
                    if i['I'][a]==number:
                        i['I'][a]=0
                    if i['N'][a]==number:
                        i['N'][a]=0
                    if i['G'][a]==number:
                        i['G'][a]=0
                    if i['O'][a]==number:
                        i['O'][a]=0
                if check_bingo(i)==True:
                    bingo=True
            y+=1
        countlist.append(y)
        x+=1
        #print(countlist)
    minn = min(countlist)
    maxx = max(countlist)
    avg = (sum(countlist)/k)

    return minn, maxx, avg 


#####################################################    
# There is no code to modify below this point.
#####################################################


def print_card(card):
    ''' Prints a Bingo card.
    
        Keyword arguments:
        
            card: a dictionary where the keys are the 
                  strings 'B', 'I', 'N', 'G', and 'O'.
                  The values for each key is a list of
                  five integers, where the values for
                  the key 'B' are in the range 1 to 15,
                  the values for key 'I' are in the range
                  16 to 30, etc.
                  
        Returns: None
    '''
    
    # Quick checks to see if card dictionary is in
    # correct format.
    if len(card) == 0:
        return
    
    for key in 'BINGO':
        if key not in card.keys():
            print('Error: problem with keys in card dictionary.')
            print('card:', card)
            return
            
        if len(card[key]) != 5:
            print('Error: problem with values in card dictionary.')
            print('card:', card)
            return
            
    
    # Get the values (list of integers) for each key.
    b = card['B']
    i = card['I']
    n = card['N']
    g = card['G']
    o = card['O']
   
    # Print header of Bingo card. 
    print('%2s  %2s  %2s  %2s  %2s' \
          %('B', 'I', 'N', 'G', 'O'))
    
    # Print values of Bingo card.
    for j in range(5): 
        print('%2d  %2d  %2d  %2d  %2d' \
              %(b[j], i[j], n[j], g[j], o[j]))


def open_file_command(file_name):
    ''' Returns a Bingo card read from a file.
    
        Keyword arguments:
        
            file_name: the name of a Bingo CSV file to open
            
        Returns:
            a dictionary representation of a Bingo card (as described 
            in check_bingo() and generate_random_card() functions).
    '''
    
    card = {}
    file_data = open(file_name).readlines()
    for line in file_data[1:]:
        nums = [int(i) for i in line.split(',')]
        for index, key in enumerate('BINGO'):
            if key in card:
                card[key] += [nums[index]]    
            else:
                card[key] = [nums[index]]
    return card

    
  
def main():
    ''' The main driver of the program. '''
    
    done = False
    
    while not done:
        user_input = input('> ')
        if user_input == 'random':
            card = generate_random_card()
            print_card(card)
            
        elif 'open' in user_input:
            file_name = user_input.split()[-1]
            card = open_file_command(file_name) 
            print_card(card)
            print('\nBingo:', check_bingo(card))
                
        elif 'sim' in user_input:
            command, n_cards, trials = user_input.split()
            minn, maxx, avg = simulate_bingo(int(n_cards), int(trials))
            print('Minimum: %.1f' %(minn))
            print('Maximum: %.1f' %(maxx))
            print('Average: %.1f' %(avg))
            
        elif user_input == 'quit':
            done = True
            
 
main()