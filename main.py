from art import logo

from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

def deal_card():
  position = random.randint(0, len(cards)-1)
  return(cards[position])

def calculate_score(li):
  if len(li) == 2 and 11 in li and 10 in li:
    return(0)
  elif sum(li) > 21 and 11 in li:
    for pos in range(len(li)):
      number = li[pos]
      if number == 11:
        li[pos] = 1
    return(sum(li))
  else:
    return(sum(li))

def compare(userscore, computerscore):
  if userscore == computerscore:
    print("Draw")
  elif userscore == 0:
    print("You win!")
  elif computerscore == 0:
    print("You lose")
  elif userscore > 21:
    print("You lose")
  elif computerscore > 21:
    print("You win!")
  elif userscore > computerscore:
    print("You win!")
  elif computerscore > userscore:
    print("You lose")


game_over = False

def play_game(): 
  game_over = False
  print(logo)
  user_cards = []
  computer_cards = []
  for i in range(1, 3):
    user_cards.append(deal_card())
  for i in range(1, 3):
    computer_cards.append(deal_card())
    
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"The computer's first card: {computer_cards[0]}")
  
  if calculate_score(user_cards) == 0 or calculate_score(user_cards) > 21:
    game_over = True
  elif calculate_score(computer_cards) == 0 or calculate_score(computer_cards) > 21:
    game_over = True

  while game_over == False:
    another_card = input("Would you like to draw another card? Type 'y' or 'n'")
    if another_card == "y":
      user_cards.append(deal_card())
      user_score = calculate_score(user_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"The computer's first card: {computer_cards[0]}")
      if user_score > 21 or user_score == 0:
        game_over = True
    else:
      game_over = True
      print(f"Your final hand is {user_cards} and your final score is {user_score}")

  while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = sum(computer_cards)
  print(f"The computer's final hand is {computer_cards} and the computer's finalscore is {computer_score}")

  compare(user_score, computer_score)

  restart = input("Would you like to restart the game? Type 'y' for yes or 'n' for no.")
  if restart == 'y':
    clear()
    play_game()
  else:
    clear()

play_game()
    

