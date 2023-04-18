############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################


from art import logo
from random import randint
from replit import clear

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def pick_cards(n, original):
  if n == 2:
    i1 = cards[randint(0,12)]
    i2 = cards[randint(0,12)]
    if (i1 == 11 and i1+i2 > 21):
      i1 = 1

    if (i2 == 11 and i1+i2 > 21):
      i2 = 1
      
    picked_cards = [i1,i2]
    output = sum(picked_cards)
    return picked_cards,output

  elif n == 1:
    i1 = cards[randint(0,12)]
    if (i1 == 11 and i1+sum(picked_cards) > 21):
      i1 = 1
    picked_cards = original
    picked_cards.append(i1)
    output = sum(picked_cards)
    return picked_cards,output

  

keep_playing = True
while (keep_playing):
  keep_picking = True
  ask = input("Do you want to play a game of blackjack: Type 'y' or 'n': " )
  
  if ask == 'n': 
    keep_playing = False
    
  else: 
    clear()
    print(logo)
    player_cards = []
    dealer_cards = []
    
    [player_cards, player_sum] = pick_cards(2, player_cards)
    [dealer_cards, dealer_sum] = pick_cards(2, dealer_cards)

    print(f'Your cards: {player_cards}, current score: {player_sum}')
    print(f"Computer's first card: {player_cards[0]}")

    while(player_sum < 21 and keep_picking):
      if dealer_sum < 17:
        [dealer_cards, dealer_sum] = pick_cards(1, original = dealer_cards)
      ask = input("Type 'y' to get another card, type 'n' to pass: ")
      if ask == 'y':
        [player_cards, player_sum] = pick_cards(1, original = player_cards)
    
        # print(f'Your cards: {player_cards}, current score: {player_sum}')
        # print(f"Computer's first card: {player_cards[0]}\n")
  
        if player_sum > 21:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's cards: {dealer_cards}, current score: {dealer_sum}")
          print('You Lost!\n')
        elif player_sum == 21:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's cards: {dealer_cards}, current score: {dealer_sum}")
          print('You Won!\n')
        else:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's first card: {player_cards[0]}\n")
    
      elif ask == 'n':
        keep_picking = False
        if player_sum > dealer_sum and player_sum < 21:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's cards: {dealer_cards}, current score: {dealer_sum}")
          print('You Won!\n')
        elif player_sum < dealer_sum and dealer_sum > 21:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's cards: {dealer_cards}, current score: {dealer_sum}")
          print('You Won, your opponent went over!\n')
        elif player_sum == dealer_sum:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's cards: {dealer_cards}, current score: {dealer_sum}")
          print('Draw!\n')
        else:
          print(f'Your cards: {player_cards}, current score: {player_sum}')
          print(f"Computer's cards: {dealer_cards}, current score: {dealer_sum}")
          print('You Lost!\n')
