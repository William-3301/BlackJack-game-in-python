import random 
from replit import clear

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
wanna_play = input("Do you want to play blackjack(y/n)?")

if wanna_play == "y":
  cont = True
else:
  cont = False

while cont:
  
  user_cards = []
  dealer_cards = []
  sum_dealer = 0
  sum_user = 0
  
  dealer_cards.append(cards[random.randint(0,12)]) 
  user_cards.append(cards[random.randint(0,12)]) 
  user_cards.append(cards[random.randint(0,12)]) 

  new_card = True
  
  print("Dealer cards are:", dealer_cards)
  
  while new_card:
    print("You cards are:", user_cards)
    get_card = input("Do you want another card(y/n)?")
    if get_card == "y":
      new_card = True
      user_cards.append(cards[random.randint(0,12)]) 
      sum_user = sum(user_cards)
        
    else:
      new_card = False
    
      
 
  dealer = True
  
  if sum_user == 21:
    print("You cards are:", user_cards)
    print("You win!\n")
  
  elif sum_user > 21:
    print("You cards are:", user_cards)
    print("You lose!\n")
  
  else:
    
    while sum_dealer < 21 or sum_user > sum_dealer:
      dealer_cards.append(cards[random.randint(0,12)]) 
      sum_dealer = sum(dealer_cards)

    if sum_dealer <= 21 and sum_dealer > sum_user:
      print("You cards are:", user_cards)
      print("Dealer cards are:", dealer_cards)
      print("You lose!\n")
   
    else:
      print("You cards are:", user_cards)
      print("Dealer cards are:", dealer_cards)
      print("You win!\n")

  wanna_play = input("Do you want to play blackjack again(y/n)?")
  print("\n")
  
  if wanna_play == "y":
    cont = True
  else:
    cont = False
    
  clear()