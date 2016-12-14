#  Computes the probability of the various hands in Yahtzee.

import random


def roll_dice():
    '''Returns 5 randomly rolled dice.'''
    dice = []
    for i in range(5):
        dice += [random.randint(1,6)]
        dice1 = sorted(dice)
        dice2 = set(dice)
    #print(dice1)
    #print(dice2)
    return dice1,dice2

def three_of_a_kind(dice1,dice2):
    '''Returns True or False if the dice are three of a kind.'''
    if dice1[0] == dice1[1] and dice1[0] == dice1[2] and dice1[0] != dice1[3] and dice1[3] != dice1[4]:
        return True
    elif dice1[1] == dice1[2] and dice1[1] == dice1[3] and dice1[1] != dice1[0] and dice1[1] == dice1[4]:
        return True
    elif dice1[2] == dice1[3] and dice1[2] == dice1[4] and dice1[2] != dice1[1] and dice1[1] != dice1[0]:
        return True
    
def four_of_a_kind(dice1,dice2):
    '''Returns True or False if the dice are four of a kind.'''
    if len(dice2) == 2:
        if (dice1[0] == dice1[3] and dice1[0] != dice1[4]) or (dice1[1] == dice1[4] and dice1[0] != dice1[1]):
            return True

def full_house(dice1,dice2):
    '''Returns True of False if the dice are a full house.'''
    if len(dice2) == 2:
        if dice1[0] == dice1[1]:
            return True
        elif dice1[-1] == dice1[-2]:
            return True
    
def small_straight(dice1,dice2):
    ''' Returns True or False if the dice represent a small straight. '''
    if dice1[4] != (dice1[0]+4):
        x = 0
        for d in range(0,4):
            if dice1[d] == dice1[0]+d:
                x += 1
        if x == 4:
            return True
        x = 0
        for d in range(0,4):
            if dice1[d+1] == dice1[0]+d:
                x += 1
        if x == 4:
            return True        
                 
def large_straight(dice1,dice2):
    ''' Returns True or False if the dice represent a large straight. '''
    if dice1 == [1,2,3,4,5] or dice1 == [2,3,4,5,6]:
        return True

def yahtzee(dice1,dice2):
    ''' Returns True or False if the dice represent Yahtzee'''
    if len(dice2) == 1:
        return True        

def main():
    '''The main block of your code.'''
    rolls = int(input('> '))
    while rolls != 'quit':
        three = 0
        four = 0
        full = 0
        y = 0
        sstrt = 0
        lstrt = 0
        m = 0    
        for i in range(rolls):
            dice1, dice2 = roll_dice()
            #print(dice1)
            #print(dice2)
            #print()
            if three_of_a_kind(dice1,dice2) == True:
                three += 1         
            elif four_of_a_kind(dice1,dice2) == True:
                four += 1
            elif full_house(dice1,dice2) == True:
                full += 1
            elif small_straight(dice1,dice2) == True:
                sstrt += 1
            elif large_straight(dice1,dice2) == True:
                lstrt += 1
            elif yahtzee(dice1,dice2) == True:
                y += 1
            else:
                m += 1  
        #print(rolls)
        print()
        print('Yahtzee',str(y)+' ('+(str((y/rolls)*100))+' %)')  
        
        print('Four of a kind',str(four)+' ('+(str((four/rolls)*100))+'%)')
        
        print('Large Straight',str(lstrt)+' ('+(str((lstrt/rolls)*100))+'%)')
        
        print('Full House',str(full)+' ('+(str((full/rolls)*100))+'%)') 
        
        print('Small Straight',str(sstrt)+' ('+(str((sstrt/rolls)*100))+'%)') 
        
        print('Three',str(three)+' ('+(str((three/rolls)*100))+'%)') 
        
        print('Misc',str(m)+' ('+(str((m/rolls)*100))+'%)') 
        print()
        rolls = int(input('> '))
main()