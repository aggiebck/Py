set0 = 0
set1 = 1
set2 = 2
set3 = 4
set4 = 8
set5 = 16


print ("Question #1: Is your birthday in Set 1?", "\n",
"1 3 5 7 ""\n",
"9 11 13 15 ""\n",
"17 19 21 23 ""\n",
"25 27 29 31")

while True:
    q1 = input("Enter (n)o or (y)es: ")
    if input is not ("y","n"):
        print ('invalid input.')
        continue
print()
print ("Question #2: Is your birthday in Set 2?", "\n",
"2 3 6 7""\n",
"10 11 14 15""\n",
"18 19 22 23""\n",
"26 27 30 31")

q2 = input("Enter (n)o or (y)es: ")
print()
print ("Question #3: Is your birthday in Set 3?", "\n",
"4 5 6 7""\n",
"12 13 14 15""\n",
"20 21 22 23""\n",
"28 29 30 31")

q3 = input("Enter (n)o or (y)es: ")
print()
print ("Question #4: Is your birthday in Set 4?", "\n",

"8 9 10 11""\n",
"12 13 14 15""\n",
"24 25 26 27""\n",
"28 29 30 31")

q4 = input("Enter (n)o or (y)es: ")
print()

print ("Question #5: Is your birthday in Set 5?", "\n",
"16 17 18 19""\n",
"20 21 22 23""\n",
"24 25 26 27""\n",
"28 29 30 31")

q5 = input("Enter (n)o or (y)es: ")

if q1 == "y":
    set0 = set0 + set1

if q2 == "y": 
    set0 = set0 + set2
    
if q3 == "y":
    set0 = set0 + set3
    
if q4 == "y":
    set0 = set0 + set4

if q5 == "y":
    set0 = set0 + set5
    
print ("Your Birthday is: ", set0)
