import random


''' 
Game Rules:-

official rules from world Rock, Paper, scissors
https://www.wrpsa.com/the-official-rules-of-rock-paper-scissors/ 

'''

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
system_Pick = [rock,paper,scissors]
user_choice = eval(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
system_choice = random.choice(system_Pick)

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

print("Computer choose: ")
print(system_choice)

if (system_choice == rock and user_choice == 0) or \
   (system_choice == paper and user_choice == 1) or \
   (system_choice == scissors and user_choice == 2):
  
  print("Tie")
elif (system_choice == rock and user_choice == 1) or \
     (system_choice == paper and user_choice == 2) or \
     (system_choice == scissors and user_choice == 0):
  print("You Win")
elif (system_choice == paper and user_choice == 0) or \
     (system_choice == scissors and user_choice == 1) or \
     (system_choice == rock and user_choice == 2):
  print("You Lose")
else:
  print("Choose correct option")
