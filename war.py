import random

suits = ('hearts','clubs','diamonds','spades')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}

class Cards:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.allcards = []
        
        for suit in suits:
            for rank in ranks:
                ccard = Cards(suit,rank)
                self.allcards.append(ccard)
                
    def Shuffle(self):
        random.shuffle(self.allcards)
        
    def dealcard(self):
        return self.allcards.pop(0)
    
class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = [] 
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
pone = input('enter player one name: ')
ptwo = input('enter player two name: ')

player_one = Player(pone)
player_two = Player(ptwo)

new_deck = Deck()
new_deck.Shuffle()

for x in range(26):
    player_one.add_cards(new_deck.dealcard())
    player_two.add_cards(new_deck.dealcard())
    
game_on = True

round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False

        else:
            print('WAR!')
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())