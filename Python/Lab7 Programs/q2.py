def reverse_add(low, high):
    ''' Executes the reverse and add algorithm for integers
        in the range low to high. For example, if low is 10 and
        high is 50, then the function would run the reverse and add
        procedure on the numbers 10, 11, .., 49, 50. Or, the user could be interested in a single number such as 89.  In 
        this case, low and high are both 89.
    '''
    
    # Write the rest of your code here.
    '''print('low:', low)
    print('high:', high)'''
    a = low
    b = a
    c = int(str(b)[::-1])
    d = 0
    if low == high:
        count = 1
        while b != c:
            d = b + c
            print(str(count)+".",b,"+",c,"=",d)
            b = d
            c = int(str(b)[::-1])
            count +=1
        print()
        print(str(low)+":", "PAL", "("+str(count), "steps)") 
    else:
        while a <= high:
            count = 0
            b = a
            c = int(str(b)[::-1])
            while b != c:
                d = b + c
                b = d
                c = int(str(b)[::-1])
                count += 1
                if count == 100:
                    break
            if count < 100:
                print(str(a)+":", "PAL", "("+str(count), "steps)") 
            else:
                print(str(a)+":", "NOT PAL", "("+str(count), "steps)")
            a += 1
def main():
    ''' The program driver. '''

    # set cmd to anything except quit()
    cmd = ''
    
    # process the user commands
    cmd = input('>>> ')
    while  cmd != 'quit':
        i = 0
        while i < len(cmd) and cmd[i] != ' ':
            i += 1
        if ' ' in cmd: 
            low = int(cmd[:i+1])
            high = int(cmd[i+1:])         
        else:
            low = int(cmd)
            high = low
        reverse_add(low, high)
        cmd = input('>>> ')

main()
