#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Create player total bank roll

class player_account:
    
    def __init__(self,name,total):
        self.name = name
        self.total = total
    
    def remove_chips(self,bet):
        self.bet = bet
        print(f"Player {self.name} bets {self.bet}")
        self.total -= self.bet
        
    def add_chips_win(self):
        print(f"Player {self.name} wins {2*self.bet}")
        self.total += 2*self.bet
    
    def add_chips_tie(self):
        print(f"Player {self.name} wins {self.bet}")
        self.total += self.bet


# In[9]:


player_bank_roll = player_account("Sean",100)


# In[3]:


player_bank_role.remove_chips(20)


# In[4]:


print(player_bank_role.total)


# In[5]:


player_bank_role.add_chips()


# In[6]:


print(player_bank_role.total)


# In[3]:


#Create Single Card

values = {"Two":2 , "Three":3 , "Four":4 , "Five":5 , "Six":6 , "Seven":7 , "Eight":8 , "Nine":9 , "Ten":10 , "Jack":10 , "Queen":10 , "King":10 , "Ace":11}
ranks = {"Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" , "Jack" , "Queen" , "King" , "Ace"}
suits = {"Hearts" , "Clubs" , "Diamonds" , "Spades"}
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


# In[4]:


mycard = Card("Hearts","Two")


# In[22]:


print(mycard)


# In[5]:


#Create Deck
import random

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                card_object = Card(suit,rank)
                self.all_cards.append(card_object)
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    
    def remove_one(self):
        return self.all_cards.pop(-1)


# In[6]:


mydeck = Deck()


# In[33]:


for card in mydeck.all_cards:
    print(card)


# In[71]:


mycard = mydeck.all_cards[-1]


# In[73]:


print(mycard)


# In[ ]:





# In[7]:


#Game logic

#Ask the player if he wants to play
game_on = False
respond_boolean = True
while respond_boolean:
    respond = input("Hey, would you like to play?\n")
    respond_upper = respond.upper()

    if respond_upper == 'YES':
        print("Okay, let's get started!\n")
        respond_boolean = False
        game_on = True
    elif respond_upper == 'NO':
        print("Okay, see you whenever you want!\n")
        respond_boolean = False
    else:
        print("I don't understand, please enter YES or NO : \n")
        continue
    
while game_on:
    
    #Game setup : after each hand you need to reset all the stuff
    player_deck = []
    dealer_deck = []
    player_sum = 0
    dealer_sum= 0
    boolean = False
    mydeck.shuffle_deck()
    if player_bank_roll.total <= 0:
        print("Player has no more money left! Thank you for playing")
        game_on = False
        continue
    
    #First of all, the player has to bet something:
    print(f"Player : {player_bank_roll.name}\nTotal bank roll : {player_bank_roll.total}")
    bet_boolean = True
    while bet_boolean:
        try:
            bet = int(input("Bet something : \n"))
        except:
            print("Please enter an integer value : \n")
            continue
        else:
            if bet > player_bank_roll.total:
                print("Unvailable bet, please enter a value which is lower than Total bank roll: \n")
                continue
            elif bet <= 0:
                print("Unvailable bet, please enter a value which is greater than zero : \n")
                continue
            else:
                player_bank_roll.remove_chips(bet)
                bet_boolean = False
                
    
    #Secondly, the dealer has to give the cards:
    
    for card in range(2):
        player_deck.append(mydeck.all_cards[-card])
        player_sum += mydeck.all_cards[-card].value
        mydeck.all_cards.pop(-card)
        dealer_deck.append(mydeck.all_cards[-card])
        dealer_sum += mydeck.all_cards[-card].value
        mydeck.all_cards.pop(-card)
    print(f"Dealer deck : \n-----   {dealer_deck[1]}")
    print(f"Player deck :\n{player_deck[0]}   {player_deck[1]}")
    
    
    #Thirdly, ask if the player wants to stay or hit
    hit_boolean = True
    
    while hit_boolean:
        try:
            player_intention = input("Would you like to hit or stay? : \n")
        except:
            print("I don't understand, please enter 'HIT' or 'STAY' : \n")
        else:
            player_intention_upper = player_intention.upper()
            if player_intention_upper != 'HIT' and player_intention_upper != 'STAY':
                print("I don't understand, please enter HIT or STAY : \n")
                continue
            else:
                hit_boolean = False
                continue
        
    hit_game = False
    player_counter = 3
    if player_intention_upper == 'HIT':
        hit_game = True
        while hit_game:
            player_deck.append(mydeck.all_cards[-1])
            player_sum += mydeck.all_cards[-1].value
            mydeck.all_cards.pop(-1)
            print("Player deck : \n")
            for card in range(player_counter):
                print(f"{player_deck[card]}")
            if player_sum > 21:
                print("Sum of the player's cards greater than 21, dealer wins!\n")
                intention_boolean = True
                while intention_boolean:
                    try:
                        respond = input("Would you like to play again? : \n")
                    except:
                        print("I don't understand, please enter YES or NO : \n")
                    else:
                        respond_upper = respond.upper()
                        if respond_upper == 'YES':
                            intention_boolean = False
                            hit_game = False
                            boolean = True
                            break
                        elif respond_upper == 'NO':
                            intention_boolean = False
                            print("Okay, thanks for playing!")
                            hit_game = False
                            boolean = True
                            game_on = False
                            break
                        else:
                            print("I don't understand, please enter YES or NO : \n")
                            continue
            if hit_game != False:
                intention_hit_boolean = True
                while intention_hit_boolean:
                    try:
                        respond = input("Would you like to hit again? : \n")
                    except:
                        print("I don't understand, please enter YES or NO : \n")
                    else:
                        respond_upper = respond.upper()
                        if respond_upper == "YES":
                            intention_hit_boolean = False
                            break
                        elif respond_upper == 'NO':
                            intention_hit_boolean = False
                            hit_game = False
                            break
                        else:
                            print("I don't understand, please enter YES or NO : \n")
                player_counter += 1
    elif player_intention_upper == "STAY":
        pass
    
    
    #As fourth thing, we need to give the cards to the dealer
    
    print(f"Dealer Deck:\n{dealer_deck[0]}   {dealer_deck[1]}")
    dealer_counter = 3
    if dealer_sum > player_sum:
        print("Sum of the dealer's cards greater than the player's one, dealer wins!\n")
        intention_boolean = True
        while intention_boolean:
            try:
                respond = input("Would you like to play again? : \n")
            except:
                print("I don't understand, please enter YES or NO : \n")
            else:
                respond_upper = respond.upper()
                if respond_upper == 'YES':
                    intention_boolean = False
                    boolean = True
                    break
                elif respond_upper == 'NO':
                    intention_boolean = False
                    print("Okay, thanks for playing!")
                    boolean = True
                    game_on = False
                    break
                else:
                    print("I don't understand, please enter YES or NO : \n")
                    continue
    else:
        while dealer_sum < 21 and player_sum < 21:
            dealer_deck.append(mydeck.all_cards[-1])
            dealer_sum += mydeck.all_cards[-1].value
            print("Dealer deck: \n")
            for card in range(dealer_counter):
                print(f"{dealer_deck[card]}")
            mydeck.all_cards.pop(-1)
            dealer_counter += 1
            if dealer_sum > 21:
                print("Sum of the dealer's cards greater than 21, Player wins!\n")
                player_bank_roll.add_chips_win()
                intention_boolean = True
                while intention_boolean:
                    try:
                        respond = input("Would you like to play again? : \n")
                    except:
                        print("I don't understand, please enter YES or NO : \n")
                    else:
                        respond_upper = respond.upper()
                        if respond_upper == 'YES':
                            intention_boolean = False
                            boolean = True
                            break
                        elif respond_upper == 'NO':
                            intention_boolean = False
                            print("Okay, thanks for playing!")
                            boolean = True
                            game_on = False
                            break
                        else:
                            print("I don't understand, please enter YES or NO : \n")
                            continue
            elif dealer_sum > player_sum:
                print("Sum of the dealer's cards greater than the player's one, dealer wins!\n")
                intention_boolean = True
                while intention_boolean:
                    try:
                        respond = input("Would you like to play again? : \n")
                    except:
                        print("I don't understand, please enter YES or NO : \n")
                    else:
                        respond_upper = respond.upper()
                        if respond_upper == 'YES':
                            intention_boolean = False
                            boolean = True
                            break
                        elif respond_upper == 'NO':
                            intention_boolean = False
                            print("Okay, thanks for playing!")
                            boolean = True
                            game_on = False
                            break
                        else:
                            print("I don't understand, please enter YES or NO : \n")
                            continue
            elif dealer_sum == player_sum:
                break
            else:
                continue
        if boolean == True:
            continue
        else:
            
            #As Fifth thing, we have to check which sum is greater
            if dealer_sum <= 21 and player_sum <= 21:
                if player_sum > dealer_sum:
                    print("Sum of the player's cards greater than the dealer's one, player wins!\n")
                    player_bank_roll.add_chips_win()
                    intention_boolean = True
                    while intention_boolean:
                        try:
                            respond = input("Would you like to play again? : \n")
                        except:
                            print("I don't understand, please enter YES or NO : \n")
                        else:
                            respond_upper = respond.upper()
                            if respond_upper == 'YES':
                                intention_boolean = False
                                boolean = True
                                break
                            elif respond_upper == 'NO':
                                intention_boolean = False
                                print("Okay, thanks for playing!")
                                boolean = True
                                game_on = False
                                break
                            else:
                                print("I don't understand, please enter YES or NO : \n")
                                continue
                elif player_sum < dealer_sum:
                    print("Sum of the dealer's cards greater than the player's one, dealer wins!\n")
                    intention_boolean = True
                    while intention_boolean:
                        try:
                            respond = input("Would you like to play again? : \n")
                        except:
                            print("I don't understand, please enter YES or NO : \n")
                        else:
                            respond_upper = respond.upper()
                            if respond_upper == 'YES':
                                intention_boolean = False
                                boolean = True
                                break
                            elif respond_upper == 'NO':
                                intention_boolean = False
                                print("Okay, thanks for playing!")
                                boolean = True
                                game_on = False
                                break
                            else:
                                print("I don't understand, please enter YES or NO : \n")
                                continue
                else:
                    print("Tie!")
                    player_bank_roll.add_chips_tie()
                    while intention_boolean:
                        try:
                            respond = input("Would you like to play again? : \n")
                        except:
                            print("I don't understand, please enter YES or NO : \n")
                        else:
                            respond_upper = respond.upper()
                            if respond_upper == 'YES':
                                intention_boolean = False
                                boolean = True
                                break
                            elif respond_upper == 'NO':
                                intention_boolean = False
                                print("Okay, thanks for playing!")
                                boolean = True
                                game_on = False
                                break
                            else:
                                print("I don't understand, please enter YES or NO : \n")
                                continue
    
    #Check if the bank roll of the player is greater than zero
    
    if player_bank_roll.total <= 0:
        print("Player has no more money left! Thank you for playing")
        game_on = False
        continue


# In[8]:


len(mydeck)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




