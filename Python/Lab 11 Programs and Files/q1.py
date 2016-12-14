def read(file):
    contents = open(file)
    word = []
    sent = []
    chars = []
    for line in contents:
        l1 = line.split() #word count
        if '.' in line or '!' in line or '?' in line:
            sent.append(line)
        word.append(len(l1)) #word count
        for i in line:
            chars.append(i)
    print('Characters: ',len(chars))
    print('Sentences: ',len(sent))
    print('Words: ',sum(word)) #word count check   
def main():
    file = input('Enter a filename: ')
    print()
    read(file)
    while file != 'quit':
        print()
        file = input('Enter a filename: ')
        print()
        read(file)    
main()