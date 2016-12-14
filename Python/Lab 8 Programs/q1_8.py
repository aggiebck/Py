def convert(number_str):   
    num = number_str
    num_list = []
    word_list = []
    word_list2 = '' 
    result = ''
    eng = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    for n in num:
        num_list.append(n)
    #print(num_list) #Check
    for e in num_list:
        e1 = int(e)
        if e1 in eng:
            word_list2=word_list2+' '+str(eng[e1])  
    #print(word_list2) #Technical Check
    result = word_list2 
    return result         
def main():
    user_input = input('>>> ')
    while  user_input != 'quit':
        print(convert(user_input))
        user_input = input('>>> ')
main()