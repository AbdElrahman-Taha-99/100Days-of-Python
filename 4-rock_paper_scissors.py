import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

choice = int(input("What do you choose: 0-->Rock, 1-->paper, 2-->scissors \n"))
if choice > 2 or choice < 0:
  print("Invalid number. You lost!")
else:
  print(f"{rps[choice]}")
  
  print("Computer choice:")
  computer_choice = random.randint(0,2)
  print(f"{rps[computer_choice]}")
  
  if ((choice == 0)and(computer_choice == 2)) or ((choice == 1)and(computer_choice == 0)) or ((choice == 2)and(computer_choice == 1)): #it could be --> or choice > computer_choice
    print("You Win!")
  elif (choice == computer_choice):
    print("Tie!")
  else:
    print("You lost!")
