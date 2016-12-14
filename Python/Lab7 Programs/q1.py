def validate(password):
          a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
          b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
          c = ['0','1','2','3','4','5','6','7','8','9']
          d = ['!','@','#','$','%','^','&','*','(',')','[',']','{','}']
          number = 0
          capital = 0
          lower = 0
          special = 0
          if len(password) < 6:
                    print("Your Password is not long enough")
                    print("The Minimum is 6 characters")
                    print("Please try again")
                    main()
          if len(password) > 12:
                    print("Your Password used to many characters")
                    print("The maximum is 12 characters")
                    print("Please Try again")
                    main()
          for e in password:
                    if len(password) >=6 and len(password) <= 12:
                              if e in a:
                                        capital=1
                              if e in b:
                                        lower=1
                              if e in c:
                                        number=1
                              if e in d:
                                        special=1
          if number==1 and capital==1 and lower==1 and special==1:
                    print("Valid")
          else:
                    print("Invalid")
                                        
                              
                   
def main():
          print()
          print()
          print("Password Rules:")
          print("a) contains at least 1 letter between [A-Z],")
          print("b) contains at least 1 letter between [a-z],")
          print("c) contains at least 1 number between [0-9],")
          print("d) contains at least 1 special character from [$#@],")
          print("e) has a minimum length of 6 characters, and")
          print("f) has a maximum length of 12 characters.")
          print()
          print("-===================================================-")
          print()          
          ''' The program driver. '''
          # set cmd to anything except quit()
          cmd = ''
          # process the user commands
          cmd = input('> ')
          while  cmd != 'quit':
                    password = cmd 
                    validate(password)
                    cmd = input('> ')
                    print()
main()
