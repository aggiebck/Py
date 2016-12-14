def problem():
    var_input = int(input("Enter a number: "))
    n = var_input
    y = n
    count = 1 
    while n != 1:
        
        if n%2==0: 
            n=n//2
            print(count,".",(n * 2),"is even,divide by half:",n)
            count+=1  
        else:
            n=n*3+1
            print(count,".",n // 3,"is odd, multiply by 3 and add 1:",n)
            count+=1
        if y < n:
            y=n
    print()        
    print("Number of Steps: ",count-1)
    print("Largest number in sequence: ",y)            
problem()

