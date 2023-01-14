#print logo
from art import logo, vs
from replit import clear
import random
from game_data import data

def akount(account):
  '''takes the account and prints the formated vlaues out of the dictionary '''
  name = account["name"]
  desc = account["description"]
  ctry = account["country"]
  return f'{name}, who is a {desc}, from {ctry}'
  #access the rnadom index in the dict, and print name , add..etc

def check(guess,follow_a,follow_b):
  '''Returns true or false based on 3 arguments guess , followers of a and b'''
  if follow_a > follow_b:
    return guess =="a"
  else:
    return guess =="b"
def game():
  score =0
  print(logo)
  game_end=False
  account_b= random.choice(data)
  
  while not game_end:
    account_a = account_b
    account_b = random.choice(data)
    print(akount(account_a))
    print(vs)
    print(akount(account_b))
    
    guess = input("Who has more followers? A/B: ").lower()
    #user input to guess followers
    follow_a = account_a["follower_count"]
    follow_b = account_b["follower_count"]
  
    flag = check(guess,follow_a, follow_b)
    
    if flag:
      score += 1
      clear()
      print(logo)
      print(f"Great,Your score is {score}")
    else:
      game_end=True
      print(f"Sad to let you go,Your score is {score}")
    #loop all above
    
while input("Play a game of guessing who has more followers yes/no \n".title()).lower() =="yes":
  clear()
  game()
  
