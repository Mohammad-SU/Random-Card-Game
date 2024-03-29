# Random Card Game

# Import Python libraries
from random import randint
from time import sleep
import re

# Prints text character by character
def delay_print(text):
  for char in text:
    print(char, end="", flush=True)
    sleep(.03)

# Waits for enter key input and then calls 'delay_print'
def delay_input(text):
  delay_print(text)
  input("")

# Players can log in and enter a username which must be valid
def username():
  while True:
    delay_print("Enter a username: ")
    username = input("")
    if re.fullmatch("[\w\d_]{3,15}", username):
      break
    else:
      delay_print("Username can only contain letters, numbers and underscores and must be 3-15 characters long.")
      print("\n")
  
  return username

# Each player will have a username
delay_print("Player 1:\n")
player1 = username()

print("\n")

delay_print("Player 2:\n")
while True:
  player2 = username()
  if player2 == player1:
    delay_print("Username must be different.")
    print("\n")
  else:
    break

print("\n")
print("____________________________________________________________________________\n")

# Intro/Instructions
delay_input("Welcome, %s and %s, to the card game. Press 'enter' to continue: " % (player1, player2))
print("\n")
delay_print("You may both compete in randomly picking from 8 cards for the chosen number of rounds.")
print("\n")
delay_print("The sum of the cards will be added to your score.")
print("\n")
delay_print("If the sum is odd, 10 points are added.")
print("\n")
delay_print("If the sum is even, 5 points are taken away.")
print("\n")
delay_print("If a double is picked, you may pick a bonus card.")
print("\n")
delay_print("If there is a tie at end of the game, you may play an extra round.")
print("\n")
def card_game():

  while True:
    try:
      delay_print("How many rounds do you want to play?: ")
      chosen_rounds = int(input(""))
      break
    except Exception:
      delay_print("Invalid input.")
      print("\n")
    
  print("\n")
  delay_input("Press 'enter' to start: ")
  print("\n")

  # Main variables - will be reset if the users want to play again
  global player1_total
  global player2_total
  global round_num
  
  player1_points = 0
  player1_total = 0
  player2_points = 0
  player2_total = 0
  round_num = 1
  
  # Main loop
  def main_game():
    global player1_total
    global player2_total
    global round_num

    delay_print("============================ ROUND %s ============================\n" % (round_num))
    
    # Players press 'enter' to pick the cards. Points are added to the score
    delay_input("%s - press 'enter' to pick the cards: " % (player1))
    player1_points = card_pick()
    player1_total += player1_points
    print("\n")
    
    print("_____________________________________________________")
    
    delay_input("%s - press 'enter' to pick the cards: " % (player2))
    player2_points = card_pick()
    player2_total += player2_points
    print("\n")
    
    print("=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=")
    
    # Display points earned in this round and in the entire game so far
    
    if player1_points == 1:
      delay_print("%s has recieved: %s point\n" % (player1, player1_points))
    else:
      delay_print("%s has recieved: %s points\n" % (player1, player1_points))
    if player1_total == 1:
      delay_print("%s has in total: %s point" % (player1, player1_total))
    else:
      delay_print("%s has in total: %s points" % (player1, player1_total))
    print("\n")
    
    if player2_points == 1:
      delay_print("%s has recieved: %s point\n" % (player2, player2_points))
    else:
      delay_print("%s has recieved: %s points\n" % (player2, player2_points))
    if player2_total == 1:
      delay_print("%s has in total: %s point" % (player2, player2_total))
    else:
      delay_print("%s has in total: %s points" % (player2, player2_total))
    print("\n")
    
    # Increments 'round_num' to increase by 1 for every loop iteration
    round_num += 1
  
  # Choose random card art with 'randint' - art corresponds with 'card_num'
  def card_pick():
    
    def card_art():
      card_num = randint(0,7)
      
      if card_num == 0:
        print("""
                         ____________
                        |            |
                        |            |
                        |    0000    |
                        |   00  00   |
                        |   00  00   | 
                        |   00  00   |
                        |    0000    |
                        |            |
                        |____________|
    """, end="", flush=True)
      
      elif card_num == 1:
        print("""
                         ____________
                        |            |
                        |            |
                        |   1111     |
                        |     11     |
                        |     11     |
                        |     11     |
                        |   111111   |  
                        |            |
                        |____________|
    """, end="", flush=True)
      
      elif card_num == 2:
        print("""
                         ____________
                        |            |
                        |            |
                        |    2222    |
                        |   22  22   |
                        |      22    |
                        |     22     |
                        |   222222   |  
                        |            |
                        |____________|
    """, end="", flush=True)
     
      elif card_num == 3:
        print("""
                         ____________
                        |            |
                        |            |
                        |    3333    |
                        |   33  33   |
                        |      333   |
                        |   33  33   |
                        |    3333    |  
                        |            |
                        |____________|
    """, end="", flush=True)
     
      elif card_num == 4:
        print("""
                         ____________
                        |            |
                        |            |
                        |   44  44   |
                        |   44  44   |
                        |   444444   |
                        |       44   |
                        |       44   |  
                        |            |
                        |____________|
    """, end="", flush=True)
      
      elif card_num == 5:
        print("""
                         ____________
                        |            |
                        |            |
                        |   555555   |
                        |   55       |
                        |   55555    |
                        |       55   |
                        |   55555    |  
                        |            |
                        |____________|
    """, end="", flush=True)
      
      elif card_num == 6:
        print("""
                         ____________
                        |            |
                        |            |
                        |    6666    |
                        |   66       |
                        |   66666    |
                        |   66  66   |
                        |    6666    |  
                        |            |
                        |____________|
    """, end="", flush=True)
      
      elif card_num == 7:
        print("""
                         ____________
                        |            |
                        |            |
                        |   777777   |
                        |       77   |
                        |      77    |
                        |     77     |
                        |    77      |
                        |            |
                        |____________|
    """, end="", flush=True)
      
      return card_num

    card1 = card_art()
    card2 = card_art()
    points = card1 + card2
    print("\n")
    delay_print("The sum is %s" % (points))
    print("\n")
    
    # If sum is odd, +10 points. If even, -5 points
    if points % 2 == 0:
      points -= 5
      delay_print("Even sum: -5 points")
    else:
      points += 10
      delay_print("Odd sum: +10 points")
    
    # Extra card will be picked if 'card1' equals 'card2'
    if card1 == card2:
      print("\n")
      delay_input("A double has been picked, press 'enter' to pick a bonus card: ")
      extra_card = card_art()
      print("\n")
      delay_print("An extra %s has been picked. It will be added to the score." % (extra_card))
      points += extra_card

    return points
  
  # Runs the game for the chosen amount of rounds
  for x in range(chosen_rounds):
    main_game()
    
  # If there is a tie, the game will continue until the total score of both players are different
  while player1_total == player2_total:
    delay_print("Both players have the same total of points. New round.")
    print("\n")
    main_game()
  
  delay_print("=========================== GAME OVER ===========================\n")
  
  # Displays the winner and by how many points they won, and distinguishes singular from plural 'points'
  if player1_total > player2_total:
    winner = player1
    winning_score = player1_total
    if player1_total - player2_total == 1:
      delay_print("%s is the winner, with %s more point than %s." % (player1, player1_total - player2_total, player2))
    else:
      delay_print("%s is the winner, with %s more points than %s." % (player1, player1_total - player2_total, player2))
  
  elif player2_total > player1_total:
    winner = player2
    winning_score = player2_total
    if player2_total - player1_total == 1:
      delay_print("%s is the winner, with %s more point than %s." % (player2, player2_total - player1_total, player1))
    else:
      delay_print("%s is the winner, with %s more points than %s." % (player2, player2_total - player1_total, player1))
  
card_game()

# Ask user if they want to play the game again
while True:
  print("\n")
  delay_print("Type 'y' if you would like to play again: ")
  play_again = input("")
  if play_again == "y":
    print("\n")
    card_game()
