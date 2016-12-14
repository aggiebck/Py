def read(file):
    print()    
    contents = open(file)
    sequences = []
    headlines = [] 
    str1 = ''
    str2 = ''  
    for line in contents:
        if '>' not in line:
            str1 = line.replace('\n','')
            str2 += str1
        else:
            headlines.append(line)
            if str1 != '':
                sequences.append(str2)
                str1 = ''
                str2 = ''
    sequences.append(str2)
    seq_up = [l.upper() for l in sequences]
    #print(seq_up)
    length = []
    for i in sequences[0:]:
        len_num = len(i)
        length.append(len_num)
    total = (sum(length))
    num_seqs = len(headlines)
    print ('Report for file', file)
    print ('Number of sequences: ', len(headlines))
    print ('Total sequences length: ', total)
    print ('Maximum sequence length: ', max(length))
    print ('Minimum sequence length: ', len(min(sequences)))
    print ('Average sequence length:', (total/num_seqs))
    print()
    seq_count = 0
    for i in seq_up[0:]:
        print (headlines[seq_count].replace('\n',''))
        print ('Length: ', len(sequences[seq_count]))
        seq_count += 1             
        A = 0
        C = 0
        G = 0
        T = 0
        for char in i:
            A = i.count('A')
            C = i.count('C')
            G = i.count('G')
            T = i.count('T')
        print ('A: ', A)
        print ('C: ', C)
        print ('G: ', G)
        print ('T: ', T)
        print()
def main():
    file = input('Enter a filename: ')
    read(file)
    while file != 'quit':
        file = input('Enter a filename: ')
        read(file)    
main()
    
    
    