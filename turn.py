class Card(object):
    
    suit_options = ["Hearts","Diamonds","Clubs","Spades"]
    value_options = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

    def __init__(self,suit,int_value):
        self.suit = suit
        self.value = int_value

    def __str__(self):
        card = [self.suit,self.value]
        #string = str(self.value) + " of " + (self.suit)
        return (str(self.value) + "of" + (self.suit))
        
    def set_suit(self,suit):
        self.suit = suit

    def set_value(self,int_value):
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
    

    def is_greater_than(self,other_card_suit,other_card_int_value):
        if self.value > other_card_value:
            return True
        else:
            return False

class Deck(object):
    import random
    list_of_cards = []
    temp_list = []
    
    while len(list_of_cards) <= 52:
        card = Card(Card.suit_options[random.randint(0,3)],Card.value_options[random.randint(0,12)])
        if card not in temp_list:
            temp_list.append(card)
            temp = card
            list_of_cards.append((card.get_value(),"of",card.get_suit()))
            
    def shuffle(self):
        import random
        random.shuffle(self.list_of_cards)

    def deal(self):
        return self.list_of_cards.pop()
    
    def __str__(self):        
        print("In this deck:")
        for card in self.list_of_cards:
            print("{} {} {}".format(card[0],card[1],card[2]))
        return ("")

    def empty():
        if len(list_of_cards) == 0:
            return True
        else:
            return False
        
def find_score(player_list):
    hearts = 0
    diamonds = 0
    clubs = 0
    spades = 0
    for card in player_list:
        if card[2] == "Hearts":
            if card[0] == "Jack" or card[0] == "Queen" or card[0] == "King":
                hearts += 10
            elif card[0] == "Ace":
                hearts += 11
            else:
                hearts += card[0]        

        if card[2] == "Diamonds":
            if card[0] == "Jack" or card[0] == "Queen" or card[0] == "King":
                diamonds += 10
            elif card[0] == "Ace":
                diamonds += 11 
            else:
                diamonds += card[0]
                   
            
        if card[2] == "Clubs":
            if card[0] == "Jack" or card[0] == "Queen" or card[0] == "King":
                clubs += 10
            elif card[0] == "Ace":
                clubs += 11
            else:
                clubs += card[0]
            
                
        if card[2] == "Spades":
            if card[0] == "Jack" or card[0] == "Queen" or card[0] == "King":
                spades += 10
            elif card[0] == "Ace":
                spades += 11
            else:
                spades += card[0]
            
        totals = {"Hearts":hearts,"Diamonds":diamonds,"Clubs":clubs,"Spades":spades}

    return totals

def thirty_one():
    
    cards = Deck()
    cards.shuffle()
    player1 = []
    player2 = []
    discarded = None
    knock = False
    player = 1
    for num in range(3):
        player1.append(cards.deal())
        player2.append(cards.deal())
    ################################

    def turn(player,discarded = discarded):
            print("--------------------------------------------------------------")
            
            # display cards
            print("PLAYER ONE\nYou have:")
            for card in player:
                print("         {}".format(card))
            if discarded == None:
                print("There is no discard.")
            else:
                print("Discard: {} {} {}".format(discarded[0],discarded[1],discarded[2]))
            print("\nPLAYER ONE:")
            
            # draw a new card
            deck_discard = input("Draw from (a)deck or (d)discard pile?\n")
            if deck_discard.lower().strip() == "a":
                new_card = cards.deal()
                player.append(new_card)
            else:
                if discarded != None:
                    new_card = discarded
                    player.append(new_card)
                else:
                    print("Discard pile is empty.  Here is a card from the deck.")
                    new_card = cards.deal()
                    player.append(new_card)
            # display new card
            print("New card:  {}".format(new_card))
            
            # discard a card
            print("Which would you like to discard?")
            print("(a): {}".format(player[0]))
            print("(b): {}".format(player[1]))
            print("(c): {}".format(player[2]))
            discard = input("(d): {}\n".format(player[3]))
            if discard.lower().strip() == "a":
                discarded = player.pop(0)
            elif discard.lower().strip() == "b":
                discarded = player.pop(1)
            elif discard.lower().strip() == "c":
                discarded = player.pop(2)
            elif discard.lower().strip() == "d":
                discarded = player.pop(3)

            # display points in each suit
            print("Points:", find_score(player))

            # clear screen
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    turn(player1)

                
            # knock?
            knock_ask = input("Would you like to knock? (y/n)\n")
            if knock_ask.lower().strip() == "y":
                knock = True # exists while loop
