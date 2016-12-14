size = int(input("Rocket Size?: "))

def rocket_top_bottom():
    count_top = 0
    bslsh = "\\"
    fslsh = "/"
    size_t = ((size*2)-1)
    top_1 = 1
    top_2 = 1
    while count_top!=((size*2)-1):
        count_top += 1
        print (" "*size_t+(fslsh*top_1)+'**'+(bslsh*top_2))
        top_1+=1
        top_2+=1
        size_t-=1
rocket_top_bottom()

def segment():
    print ("+" +("=*"*(size*2))+ '+') 
segment()

def middle1():
    count_middle1 = 0
    size_m1 = ((size - 1)*2)
    mid_1 = 1
    mid_2 = 1
    dots_a = (size-1)
    bslsh = "\\"
    fslsh = "/"    
    while (count_middle1!=size):
        print("|"+("."*dots_a)+((fslsh+bslsh)*mid_1)+("."*size_m1)+((fslsh+bslsh)*mid_2)+("."*dots_a)+"|")
        mid_1+=1
        mid_2+=1        
        count_middle1+=1
        dots_a-=1
        size_m1-=2
middle1()
        
def middle2():
    count_middle2 = 0
    dots_b = 0
    dots_c = 0        
    size_m2 = (size-1)
    mid_3 = (size)
    mid_4 = (size)
    bslsh = "\\"
    fslsh = "/"    
    while (count_middle2!=size):
        print("|"+("."*dots_b)+((bslsh+fslsh)*mid_3)+("."*dots_c)+((bslsh+fslsh)*mid_4)+("."*dots_b)+"|")
        count_middle2+=1
        size_m2+=2
        mid_3-=1
        mid_4-=1        
        dots_b+=1
        dots_c+=2
middle2()
segment()
middle2()
middle1()
segment()
rocket_top_bottom()
