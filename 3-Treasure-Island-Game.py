print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("Welcome to -->Treasure Island<-- !!\n\tPress ENTER to continue...")
input()
print("Your mission is to find the treasure!!\n\tPress ENTER to start!!")
input()
decision = input("You're on an island and you have two ways to go .. Left or Right??\n").lower()
#decision = decision.lower()
if decision == "right" :
  print("You fell into a hole and died :(")
  print("\t\tGAME OVER..")
else:
  decision = input("Good job!\nNow you've reached a lake, what should you do? .. Swim or Wait??\n").lower()
  #decision = decision.lower()
  if decision == "swim" :
    print("Unfourtunately .. You are attacked by trout :(")
    print("\t\tGAME OVER..")
  else:
    print("Very Wise!\nWhile waiting you noticed a little boat and crossed the lake safely.")
    decision = input("Now you found three doors .. Red, Blue, and Yellow .. Which one you choose to enter?\n").lower()
    #decision = decision.lower()
    if decision == "red" :
      print("Ouch! .. You are burned by fire :(")
      print("\t\tGAME OVER..")
    elif decision == "blue" :
      print("Very Unlucky! .. You've awakened the beasts to be their lunch! :(")
      print("\t\tGAME OVER..")
    elif decision == "yellow" :
      print("Very lucky Choice! .. You finally found the treasure!")
      print("\t\tYOU WIN !!!!!!")
    else :
      print("Wrong Choice !!")
      print("\t\tGAME OVER..")
