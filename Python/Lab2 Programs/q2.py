NumofGuest = int(input("Number of guests: "))

option1 = 32//NumofGuest
option1rm = 32%NumofGuest
option2 = 32/NumofGuest

option1x2 = 64//NumofGuest
option1rmx2 = 64%NumofGuest
option2x2 = 64/NumofGuest

if NumofGuest >= 33:
    print("Sorry, but it looks like you need more pizza!")
    print()
    print("Option 1 with 1 extra Pizza: ", option1x2,"slice each,",option1rmx2,"left over") 
    print()
    print("Option 2 with 1 extra Pizza: ",option2x2,"slices each")
else:
    print("Option 1: ",option1,"slices each,",option1rm,"left over")
    print()
    print("Option 2: ",option2,"slices each")

