import random
from art import *
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    computer=random.choices(cards, k=2)
    user=random.choices(cards,k=2)
    return computer, user

def calculate_score(computer,user):
    sum_computer=sum(computer)
    sum_user=sum(user)
    print(f"The hand of user is {user} and current score is {sum_user}")
    print(f"Computer's first card is {computer[0]}")
    if (sum_computer<17):
        add_computer=(deal_card()[0])
        computer.append(add_computer[0])
        sum_computer=sum(computer)
    another=input("Type 'Y' to get another card and 'N' to pass: ")
    if (another.upper()=="Y"):
        add_user=(deal_card()[1])
        if (add_user==11) and (sum_user+add_user>21):
            print("You got an ACE and counted it as 1")
            user.append(1)
        elif (add_user==11) and (sum_user+add_user<21):
            print("You got an ACE")
            user.append(11)
        else:
            print(f"You got {add_user[0]}")
            user.append(add_user[0])
            sum_user=sum(user)
        print(f"The hand of user is {user} and the final score is {sum_user}")
        print(f"The hand of Computer is {computer} and the final score is {sum_computer}")
        compare(sum_user,sum_computer)
    else:
        print(f"The hand of user is {user} and the final score is {sum_user}")
        print(f"The hand of Computer is {computer} and the final score is {sum_computer}")
        compare(sum_user,sum_computer)

def compare(sum_user,sum_computer):
    if (sum_user>21 and sum_computer<=21) or ((sum_computer<=21) and (sum_user<sum_computer))  :
        print("Sorry! You have lost.☹️") 
    elif ((sum_user<=21) and (sum_user>sum_computer)) or (sum_user<=21 and sum_computer>21) :
        print("Congratulations! You have won.😉")
    else:
        print("Draw..Noone Wins!!")
def blackjack():
  while True:
    ask=input("Do you want to play BlackJack?(Y/N) ")
    if (ask.upper()=="Y"):
      print(logo)
      computer=(deal_card()[0])
      user=(deal_card()[1])
      calculate_score(computer,user)
      ask_again=input("Do you want to play again?(Y/N) ")
      if (ask_again.upper()=="Y"):
        continue
      else:
        break
    else:
      print("See You!👋")
      break
      

if __name__ == "__main__":
    blackjack()


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

