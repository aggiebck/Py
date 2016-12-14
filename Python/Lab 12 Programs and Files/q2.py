import math

def log(b,r):
    
    print('-----------------------------')
    print('%    Months to payoff balance')
    print('-----------------------------')
    per = 1
    c = 25
    while c > 0:       
        p = (per/100)*b
        rate = (r/100)/12
        num = (1-((b*rate)/p))
        #print(math.log(num))
        denum = (1+rate) 
        #print(math.log(denum))
        if num <=0 or denum <=0:
            print(per,' ','<Undefined>')
        else:
            n = -((-(math.log(num))))/(-(math.log(denum)))
            print(per,' ',round(n,1))
        per += 1
        c -= 1
        
def main():
    b = float(input('Credit card balance ($):'))
    r = float(input('Annual Percentage Rate (%):'))
    print()
    log(b,r)
    while b != 'quit' and r != 'quit':
        b = float(input('Credit card balance ($):'))
        r = float(input('Annual Percentage Rate (%):'))
        print()
        log(b,r)
main()
        
        
        