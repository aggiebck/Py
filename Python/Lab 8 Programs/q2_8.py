def convert(number_str):
    low = {0 : '',1 : 'one',2 : 'two',3 : 'three',4 : 'four',5 : 'five',6 : 'six',7 : 'seven',8 : 'eight',9 : 'nine',10 : 'ten',20 : 'twenty',30 : 'thirty',40 : 'forty',50 : 'fifty',60 : 'sixty',70 : 'seventy',80 : 'eighty',90 : 'ninety'}
    
    teens = {11 : 'eleven',12 : 'twelve',13 : 'thirteen',14 : 'fourteen',15 : 'fifteen',16 : 'sixteen',17 : 'seventeen',18 : 'eighteen',19 : 'nineteen'}
    
    num = number_str
    numint = int(num)
    numlist = []
    
    numint_t = numint//1000
    #print(numint_t)
    numint_h = (numint//100)-(numint_t*10)
    #print(hundreds)
    tens = (numint//10)-(numint_h*10)-(numint_t*100)
    #print(tens)
    ones = numint%10
    #print(ones)
    
    #print('tens '+str(tens)) #testing
    #print(tens*10+ones) #testing
    if len(num) == 1:
        return low.get(numint)
    elif len(num) == 2 and numint in teens:
        return teens.get(numint)
    elif len(num) == 2:
        if ones != 0:
            return (low.get(tens*10) +' '+ low.get(ones))
        elif ones == 0:
            return (low.get(numint))
    if len(num) == 3:    
        hundred = (str(low.get(numint_h))+' '+'hundred')
        if ones == 0 and tens == 0:
            return (hundred)
        elif ones != 0 and tens != 0 and tens != 1:
            #print('a')
            return (str(hundred) +' and '+ str(low.get(tens*10)) +' '+ str(low.get(ones)))
        elif tens == 1:
            #print('b')
            return (str(hundred) +' and '+ str(teens.get(tens*10+ones)))
        elif tens == 0:
          	#print('c')
          	return (str(hundred) +' and '+ str(low.get(ones)))
        elif ones == 0:
          	#print('d')
          	return (str(hundred) +' and '+ str(low.get(tens*10)))
    if numint_t == 0: 
    	print('Invalid Number, Please try again')
    	main()    
    if len(num) == 4:
    	result = (str(low.get(numint_t))+' thousand')
    	hundred = (str(low.get(numint_h))+' '+'hundred')
    	if numint_h != 0:
    		result = result+' '+str(hundred)
    	if tens != 0 and tens != 1:
    		result = result+' '+str(low.get(tens*10))
    	if tens == 1:
    		result = result+' '+str(teens.get(tens*10+ones))
    	if ones != 0 and tens != 1:
    		result = result+' '+str(low.get(ones))
    return result

        
def main():
    user_input = input('>>> ')
    while  user_input != 'quit':
        print(convert(user_input))
        user_input = input('>>> ')
main()