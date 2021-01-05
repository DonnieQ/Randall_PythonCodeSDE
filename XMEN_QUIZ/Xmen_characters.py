#!/usr/bin/env python3

Xmen_Mutants = {
'Wolverine': [1, 3, 4, 8, 10],
'Storm': [3, 10, 15, 7, 9],
'Cyclops':[5, 3, 7, 8, 1],
'Rogue':[2, 3, 5, 6, 11],
'Beast':[10, 3, 9, 8, 12]}

message = 'Which X-men Mutant are you?'
message2= 'Your X-men mutant is '
a=list(range(10))
while True:
     try:
        print(message)
        power= str(input("Are you aggressive or reserved? Yes or no?"))
        ability= str(input("Would you say you were smart? Yes or no?"))
        fly= str(input("Do you like heights? Yes or no?"))
        Mutant_Level= str(input("Would you say your a threat? Yes or no?"))
        Behavior= str(input("Do you like helping others? Yes or no?"))
        break

     except:
        print("Please use your words.")

if power == "yes":
    a.append(1)
elif power == "no":
    a.append(2)
if ability == "yes":
    a.append(1)
elif ability =="no":
    a.append(2)
if a[1]:
    message2 = message2 + 'Storm'
if a[2]:
   messge2 = message2 + 'Wolverine'
else:
    print("this game is under construction")
print(message2)

