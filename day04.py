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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2: "))
if choice == 0:
    print(f"You chose: Rock {rock}")
elif choice == 1:
    print(f"You chose: Paper {paper}")
elif choice == 2:
    print(f"You chose: Scissors {scissors}")


computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer Chose: Rock")
    print(rock)
    if choice == 0:
        print("It's a Draw")    
    elif choice == 2:
        print("You loose!")
    else:
        print("You win!")
elif computer_choice == 1:
    print("Computer Chose: Paper")
    print(paper)
    if choice == 1:
        print("It's a Draw")    
    elif choice == 0:
        print("You loose!")
    else:
        print("You win!")
elif computer_choice == 2:
    print("Computer Chose: Scissors")
    print(scissors)
    if choice == 2:
        print("It's a Draw")    
    elif choice == 1:
        print("You loose!")
    else:
        print("You win!")