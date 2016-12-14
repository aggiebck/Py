import csv

def baby_names(start, finish, sex):
    file = open("TX.csv", 'r')
    fieldnames = ["State", "Sex", "Year", "Name", "Amount"]
    raw_rows = csv.DictReader(file, fieldnames = fieldnames)
    strtl = []
    finl = []
    
    
    
    
def main ():
    cmd = input('>')
    sex = 'M'
    while cmd != 'quit()':
        cmd = input('>')
        if cmd == 'boy':
            sex = 'M'
        elif cmd == 'girl':
            sex = 'F'
        else:
            start,finish = str.split(cmd)    
            baby_names(start, finish, sex)
        
main()
        
