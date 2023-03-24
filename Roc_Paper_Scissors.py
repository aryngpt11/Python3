import random

Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice=int(input("Enter the no 0 for rock,1 for scissors,2 for paper: "))
if user_choice==0:
    print(Rock)
elif user_choice==1:
    print(Scissors)
elif user_choice==2:
    print(Paper)
else:
    print("Type a valid no")
Comp_choice=random.randint(0,2)
print(f"Computer choose {Comp_choice}")
if Comp_choice==0:
    print(Rock)
elif Comp_choice==1:
    print(Scissors)
else:
    print(Paper)

if user_choice==1 & Comp_choice==2:
    print("You Wins!")
elif Comp_choice>user_choice:
    print("You lose ")
elif Comp_choice==user_choice:
    print("Match Draw")
else:
    print(" you lose")