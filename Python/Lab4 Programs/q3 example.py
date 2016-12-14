size = int(input('Size: '))

# This is the code for the top of the rocket
# top = size * 2 - 1

count_top = 0
backslash = '\\'
forwardslash = '/'
size_b = ((size*2)-1)
a = 1
b = 1
while (count_top != ((size*2)-1)):

        count_top += 1
        print(' ' * size_b + (forwardslash * a) + '**' + (backslash * b))
        a += 1
        b += 1
        size_b -= 1        
	
# This is the code for the separation lines in the body of the rocket
# separationlines = size * 2 with symbols + * = +
        
print ('+'+('=*'*(size*2))+'+')

# This is the code for the body of the rocket 
# body = multiples of 2 up to size * 2

count_body = 0
c = 1
d = 1
size_c = (size + 1)
dotcount = 2
while (count_body != size):
        
        print('|'+ ('.'*dotcount)+((forwardslash+backslash)*c)+('.'*size_c)+((forwardslash+backslash)*d)+('.'*dotcount)+'|')
        c += 1
        d += 1
        count_body += 1
        dotcount -= 1
        size_c -= 2

# This is the code for the upside down body of the rocket 
# body = multiples of 2 up to size * 2
    
count_body = 0
e = 3
f = 3
size_d = (size - 1)
dotcount_b = 0
dotcount_c = 0
while (count_body != size):
        
        print('|'+ ('.'*dotcount_b)+((backslash+forwardslash)*e)+('.'*dotcount_c)+((backslash+forwardslash)*f)+('.'*dotcount_b)+'|')
        e -= 1
        f -= 1
        count_body += 1
        dotcount_b += 1
        dotcount_c += 2
        size_d += 2

# This is the code for the separation lines in the body of the rocket
# separationlines = size * 4 with symbols + * = +

print ('+'+('=*'*(size*2))+'+')
        
# This is the code for the upside down body of the rocket 
# body = multiples of 2 up to size * 2
    
count_body = 0
e = 3
f = 3
size_d = (size - 1)
dotcount_b = 0
dotcount_c = 0
while (count_body != size):
        
        print('|'+ ('.'*dotcount_b)+((backslash+forwardslash)*e)+('.'*dotcount_c)+((backslash+forwardslash)*f)+('.'*dotcount_b)+'|')
        e -= 1
        f -= 1
        count_body += 1
        dotcount_b += 1
        dotcount_c += 2
        size_d += 2
        
# This is the code for the body of the rocket 
# body = multiples of 2 up to size * 2
    
count_body = 0
c = 1
d = 1
size_c = (size + 1)
dotcount = 2
while (count_body != size):
            
        print('|'+ ('.'*dotcount)+((forwardslash+backslash)*c)+('.'*size_c)+((forwardslash+backslash)*d)+('.'*dotcount)+'|')
        c += 1
        d += 1
        count_body += 1
        dotcount -= 1
        size_c -= 2


# This is the code for the separation lines in the body of the rocket
# separationlines = size * 2 with symbols + * = +
            
print ('+'+('=*'*(size*2))+'+')


# This is the code for the bottom of the rocket
# bottom = top

count_top = 0
size_b = ((size*2)-1)
a = 1
b = 1
while (count_top != ((size*2)-1)):

        count_top += 1
        print(' ' * size_b + (forwardslash * a) + '**' + (backslash * b))
        a += 1
        b += 1
        size_b -= 1        
