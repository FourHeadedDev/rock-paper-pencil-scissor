'''
rock = 0 
paper = 1
pncil = 2
scissor =3 
'''

import random

from colorama import Fore, Style, init
init(autoreset=True)




dict = { "0" : " rock",
         "1" : " paper",
         "2" : " pencil",
         "3" : " scissor"}

ascii_art = {
    0: '''
    ROCK 🪨
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',

    1: '''
    PAPER 📄
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',

    2: '''
    PENCIL ✏️
        _______
    ---'   ____)
           |   |
           |   |
           |___|
    ---.________)
    ''',

    3: '''
    SCISSOR ✂️
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
} #this dictionary i got from chat gpt 


user_name = input("Enter your name: ") 

rounds = int(input("Enter number of rounds you want to play: "))
user_score = 0
computer_score = 0

for i in range(rounds):
    print(f"Round {i + 1} of {rounds}")
    You = int(input( Fore.CYAN + "Enter 0 for rock, 1 for paper, 2 for pencil, 3 for scissor: "))
    computer = random.choice([0, 1, 2, 3])
    print(f"{user_name}  chose {You} {dict[str(You)]}")
    print(ascii_art[You])
    print(f"Computer chose {computer} {dict[str(computer)]}")
    print(ascii_art[computer])
    if You < 0 or You > 3:
        print("Invalid input! Please enter a number between 0 and 3.")
        continue
    
    if You == computer:
        print(Fore.YELLOW , "It's a tie!")
    else:
        if (You == 0 and computer ==2) or (You == 0 and computer == 3 ) or (You == 1 and computer == 0) or (You == 2 and computer == 1) or (You == 3 and computer == 1 ):
            print(Fore.GREEN , f"{user_name} You win!")
            user_score += 1
        else:
            print(Fore.RED , "Computer wins!")
            computer_score += 1

print( Fore.CYAN ,"final scores")
print(f"{Fore.MAGENTA}{user_name} score: {user_score}")
print(f"{Fore.MAGENTA} Computer score: {computer_score}")








