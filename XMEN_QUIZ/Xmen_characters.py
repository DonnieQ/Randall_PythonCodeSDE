#!/usr/bin/env python3

Xmen_Mutants = {
'Wolverine': [1, 2, 1, 1, 2],
'Storm': [1, 1, 1, 1, 1],
'Cyclops':[2, 1, 2, 2, 1],
'Rogue':[1, 1, 1, 2, 1],
'Beast':[2, 1, 2, 1, 1]}

message = 'Which X-men Mutant are you?'
message2= 'Your X-men mutant is '
a=[]
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
if fly == "yes":
    a.append(1)
elif fly == "no":
    a.append(2)
if Mutant_Level == "yes":
    a.append(1)
elif Mutant_Level == "no":
    a.append(2)
if Behavior == "yes":
    a.append(1)
elif Behavior == "no":
    a.append(2)
if a[1]:
    message2 = message2 + 'Storm'
if a[2]:
   messge2 = message2 + 'Wolverine'
else:
    print("this game is under construction")
print(message2)

