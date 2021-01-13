from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheating_Larry

cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()
cheater3 = Cheating_Larry()
#inherits roll from player class
cheater1.roll()
cheater2.roll()
cheater3.roll()

cheater1.cheat()
cheater2.cheat()
cheater3.cheat()
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))
print("Uncle Larry rolled"  + str(cheater3.get_dice()))
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()) & sum(cheater3.get_dice()):
  print("Draw! Everyones a Winner!!\n Uncle Larry is disgruntled")
  with open('/home/student/Randall_PythonCodeSDE/oop2/uncle_larry.txt', 'r') as f:
    print(f.read())

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()) | sum(cheater3.get_dice()):
  print("Cheater 1 wins!\n Uncle larry's eyes shoots lazers")
  with open('/home/student/Randall_PythonCodeSDE/oop2/uncle_unhappy.txt', 'r') as f:
    print(f.read())
elif sum(cheater2.get_dice()) > sum(cheater1.get_dice()) | sum(cheater3.get_dice()):
  print("Cheater 2 wins!\n What!!??? Uncle Larry has evolved into Charizard!!!")
  with open('/home/student/Randall_PythonCodeSDE/oop2/uncle_charizard.txt', 'r') as f:
    print(f.read())
elif sum(cheater3.get_dice()) > sum(cheater1.get_dice()) | sum(cheater2.get_dice()):
  print("Uncle Larry is the Winner!!")
  with open('/home/student/Randall_PythonCodeSDE/oop2/uncle_wins.txt', 'r') as f:
    print(f.read())
else:
  print("Uncle Larry Wins!!\n and it's not because im scared!!")
  with open('/home/student/Randall_PythonCodeSDE/oop2/uncle_scary.txt', 'r') as f:
    print(f.read())
