# SimpleCard class
class SimpleCard(object):
    value_options = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

    def __init__(self,value):
        self.value = value

    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def is_greater_than(self,other_card):

        try:
            if int(self.value) > int(other_card.get_value()):
                return True
            else:
                return False
        except ValueError:
            if self.value == "Jack" or self.value == "Queen" or self.value == "King":
                val1 = 10
            elif self.value == "Ace":
                val1 = 11
            if other_card.get_value == "Jack" or other_card.get_value == "Queen" or other_card.get_value == "King":
                val2 = 10
            elif other_card.get_value == "Ace":
                val2 = 11
            if val1 > val2:
                return True
            else:
                return False
# Card class        
class Card(SimpleCard):
    
    suit_options = ["Hearts","Diamonds","Clubs","Spades"]

    def __init__(self,value,suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        card = [self.suit,self.value]
        #string = str(self.value) + " of " + (self.suit)
        return "{} of {}".format(self.value,self.suit)
        
    def set_suit(self,suit):
        self.suit = suit

    def get_suit(self):
        return self.suit
    
    
# Deck class
class Deck(object):
    import random
    list_of_cards = []

    def __init__(self):
        for suit in Card.suit_options:
            for value in SimpleCard.value_options:
                card = Card(suit,value)
                self.list_of_cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.list_of_cards)

    def deal(self):
        return self.list_of_cards.pop()
    
    def __str__(self):        
        print("In this deck:")
        for card in self.list_of_cards:
            print("{}".format(card.get_value))
        return ("")

    def __repr__(self):
        return self.__str__()

    def empty():
        if len(list_of_cards) == 0:
            return True
        else:
            return False

# SimpleDeck:
class SimpleDeck(Deck):
    import random
    list_of_cards = []

    def __init__(self):
        for suit in range(4):
            for value in SimpleCard.value_options:
                card = SimpleCard(value)
                self.list_of_cards.append(card)

# assorted methods        
def find_score(player_list):
    hearts = 0
    diamonds = 0
    clubs = 0
    spades = 0
    for card in player_list:
        if card.get_suit() == "Hearts":
            if card.get_value() == "Jack" or card.get_value() == "Queen" or card.get_value() == "King":
                hearts += 10
            elif card.get_value() == "Ace":
                hearts += 11
            else:
                hearts += card.get_value()        

        if card.get_suit() == "Diamonds":
            if card.get_value() == "Jack" or card.get_value() == "Queen" or card.get_value() == "King":
                diamonds += 10
            elif card.get_value() == "Ace":
                diamonds += 11 
            else:
                diamonds += card.get_value()
                   
            
        if card.get_suit() == "Clubs":
            if card.get_value() == "Jack" or card.get_value() == "Queen" or card.get_value() == "King":
                clubs += 10
            elif card.get_value() == "Ace":
                clubs += 11
            else:
                clubs += card.get_value()
            
                
        if card.get_suit() == "Spades":
            if card.get_value() == "Jack" or card.get_value() == "Queen" or card.get_value() == "King":
                spades += 10
            elif card.get_value() == "Ace":
                spades += 11
            else:
                spades += card.get_value()
            
    totals = {hearts:"Hearts",diamonds:"Diamonds",clubs:"Clubs",spades:"Spades"}
    string = "{} in Hearts, {} in Diamonds, {} in Clubs, {} in Spades".format(hearts,diamonds,clubs,spades)
    maxi = max(totals)
    return "{} in {}".format(maxi, totals[maxi])

def ante(player1,player2):
    print("Ante")
    facedown1_1 = player1.pop(0)
    facedown2_1 = player1.pop(0)
    ante_1 = player1.pop(0)
    facedown1_2 = player2.pop(0)
    facedown2_2 = player2.pop(0)
    ante_2 = player2.pop(0)
    print("Player 1:", ante_1,"\nPlayer 2:",ante_2)
    if ante_1 == ante_2 and len(player1) > 0 and len(player2) > 0:
        ante(player1,player2)
    elif len(player1) <= 0:
        return "player1"
    elif len(player2) <= 0:
        return "player2"

    
def simple_war():
    cards = SimpleDeck()
    cards.shuffle()
#    assert cards.isinstance(Deck()), "not a Deck"
    player1 = []
    player2 = []
    for num in range(26):
        player1.append(cards.deal())
        player2.append(cards.deal())
        
    while len(player1) > 0 and len(player2) > 0:
##        p1card = player1.pop(0)
##        p2card = player2.pop(0)
##        print("Player 1:", p1card)
##        print("Player 2:", p2card)
##        
##        if p1card.is_greater_than(p2card):
##            print("Player 1 gets the cards.")
##            player1.append(p1card)
##            player1.append(p2card)
##        elif p2card.is_greater_than(p1card):
##            print("Player 2 gets the cards.")
##            player2.append(p1card)
##            player2.append(p2card)
##        else:
        ante(player1,player2)
        
    
def full_war():
    cards = Deck()
    cards.shuffle()
    assert cards.isinstance(Deck()), "not a Deck"
    player1 = []
    player2 = []
    for num in range(26):
        player1.append(cards.deal())
        player2.append(cards.deal())

### Game: Thirty One
##def thirty_one():
##    # variables
##    
##    cards = Deck()
##    cards.shuffle()
##    player1 = []
##    player2 = []
##    discarded = None
##    knock = False
##    player = 1
##    
##    # populate hands
##    for num in range(3):
##        player1.append(cards.deal())
##        player2.append(cards.deal())
##
##    # clear screen
##    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")    
##
##    # RUN "NORMAL" GAME
##    while knock == False:
##        
##        # who goes?
##        # player one goes
##        if player == 1:
##            print("--------------------------------------------------------------")
##            
##            # display cards
##            print("PLAYER ONE\nYou have:")
##            for card in player1:
##                print("         {}".format(card))
##            if discarded == None:
##                print("There is no discard.")
##            else:
##                print("Discard: {}".format(discarded))
##            print("\nPLAYER ONE:")
##            
##            # draw a new card
##            deck_discard = input("Draw from (a)deck or (d)discard pile?\n")
##            if deck_discard.lower().strip() == "a":
##                new_card = cards.deal()
##                player1.append(new_card)
##            else:
##                if discarded != None:
##                    new_card = discarded
##                    player1.append(new_card)
##                else:
##                    print("Discard pile is empty.  Here is a card from the deck.")
##                    new_card = cards.deal()
##                    player1.append(new_card)
##            # display new card
##            print("New card:  {}".format(new_card))
##            
##            # discard a card
##            print("Which would you like to discard?")
##            print("(a): {}".format(player1[0]))
##            print("(b): {}".format(player1[1]))
##            print("(c): {}".format(player1[2]))
##            discard = input("(d): {}\n".format(player1[3]))
##            if discard.lower().strip() == "a":
##                discarded = player1.pop(0)
##            elif discard.lower().strip() == "b":
##                discarded = player1.pop(1)
##            elif discard.lower().strip() == "c":
##                discarded = player1.pop(2)
##            elif discard.lower().strip() == "d":
##                discarded = player1.pop(3)
##
##            # display points in each suit
##            print("Most points:", find_score(player1))
##            
##            # knock?
##            knock_ask = input("Would you like to knock? (y/n)\n")
##            if knock_ask.lower().strip() == "y":
##                knock = True # exists while loop
##            player = 2
##
##            # clear screen
##            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
##            
##        # player two goes
##        elif player == 2:
##            print("--------------------------------------------------------------")
##            
##            # display cards
##            print("PLAYER TWO\nYou have:")
##            for card in player2:
##                print("         {}".format(card))
##            if discarded == None:
##                print("There is no discard.")
##            else:
##                print("Discard: {}".format(discarded))
##            print("\nPLAYER TWO:")
##            
##            # draw a new card
##            deck_discard = input("Draw from (a)deck or (d)discard pile?\n")
##            if deck_discard.lower().strip() == "a":
##                new_card = cards.deal()
##                player2.append(new_card)
##            else:
##                if discarded != None:
##                    new_card = discarded
##                    player2.append(new_card)
##                else:
##                    print("Discard pile is empty.  Here is a card from the deck.")
##                    new_card = cards.deal()
##                    player2.append(new_card)
##            # display new card
##            print("New card:  {}".format(new_card))
##            
##            # discard a card
##            print("Which would you like to discard?")
##            print("(a): {}".format(player2[0]))
##            print("(b): {}".format(player2[1]))
##            print("(c): {}".format(player2[2]))
##            discard = input("(d): {}\n".format(player2[3]))
##            if discard.lower().strip() == "a":
##                discarded = player2.pop(0)
##            elif discard.lower().strip() == "b":
##                discarded = player2.pop(1)
##            elif discard.lower().strip() == "c":
##                discarded = player2.pop(2)
##            elif discard.lower().strip() == "d":
##                discarded = player2.pop(3)
##
##            # display points in each suit
##            print("Most points:", find_score(player2))
##            
##            # knock?
##            knock_ask = input("Would you like to knock? (y/n)\n")
##            if knock_ask.lower().strip() == "y":
##                knock = True # exists while loop
##            player = 1
##
##            # clear screen
##            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
##            
##    # RUN "KNOCKED" GAME
##    # who goes
##    # player one goes
##    if player == 1:
##        print("--------------------------------------------------------------")
##        
##        # display cards
##        print("PLAYER ONE\nLAST TURN\nYou have:")
##        for card in player1:
##            print("         {}".format(card))
##        if discarded == None:
##            print("There is no discard.")
##        else:
##            print("Discard: {}".format(discarded))
##        print("\nPLAYER ONE:")
##        
##        # draw a new card
##        deck_discard = input("Draw from (a)deck or (d)discard pile?\n")
##        if deck_discard.lower().strip() == "a":
##            new_card = cards.deal()
##            player1.append(new_card)
##        else:
##            if discarded != None:
##                new_card = discarded
##                player1.append(new_card)
##            else:
##                print("Discard pile is empty.  Here is a card from the deck.")
##                new_card = cards.deal()
##                player1.append(new_card)
##        # display new card
##        print("New card:  {}".format(new_card))
##        
##        # discard a card
##        print("Which would you like to discard?")
##        print("(a): {}".format(player1[0]))
##        print("(b): {}".format(player1[1]))
##        print("(c): {}".format(player1[2]))
##        discard = input("(d): {}\n".format(player1[3]))
##        if discard.lower().strip() == "a":
##            discarded = player1.pop(0)
##        elif discard.lower().strip() == "b":
##            discarded = player1.pop(1)
##        elif discard.lower().strip() == "c":
##            discarded = player1.pop(2)
##        elif discard.lower().strip() == "d":
##            discarded = player1.pop(3)
##
##
##        # clear screen
##        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
##
##        
##    # player two goes    
##    if player == 2:
##            print("--------------------------------------------------------------")
##            
##            # display cards
##            print("PLAYER TWO\nLAST TURN\nYou have:")
##            for card in player2:
##                print("         {}".format(card))
##            if discarded == None:
##                print("There is no discard.")
##            else:
##                print("Discard: {}".format(discarded))
##            print("\nPLAYER TWO:")
##            
##            # draw a new card
##            deck_discard = input("Draw from (a)deck or (d)discard pile?\n")
##            if deck_discard.lower().strip() == "a":
##                new_card = cards.deal()
##                player2.append(new_card)
##            else:
##                if discarded != None:
##                    new_card = discarded
##                    player2.append(new_card)
##                else:
##                    print("Discard pile is empty.  Here is a card from the deck.")
##                    new_card = cards.deal()
##                    player2.append(new_card)
##            # display new card
##            print("New card:  {}".format(new_card))
##            
##            # discard a card
##            print("Which would you like to discard?")
##            print("(a): {}".format(player2[0]))
##            print("(b): {}".format(player2[1]))
##            print("(c): {}".format(player2[2]))
##            discard = input("(d): {}\n".format(player2[3]))
##            if discard.lower().strip() == "a":
##                discarded = player2.pop(0)
##            elif discard.lower().strip() == "b":
##                discarded = player2.pop(1)
##            elif discard.lower().strip() == "c":
##                discarded = player2.pop(2)
##            elif discard.lower().strip() == "d":
##                discarded = player2.pop(3)
##
##            # clear screen
##            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
##
##        
##    # GAME FINISHED; PRINT RESULTS
##    # scores
##    print("Game over")
##    first_temp = find_score(player1)
##    second_temp = find_score(player2)
##    print("Player 1:",first_temp)
##    print("Player 2:",second_temp)
##    
##    # winner
##    first = first_temp.split()
##    second = second_temp.split()
##    
##    if int(first[0]) < int(second[0]):
##        print("Player 2 won!")
##    elif int(first[0]) > int(second[0]):
##        print("Player 1 won!")
##    else:
##        print("It was a tie!")
##        
##games_list = [("thirty_one()",2,"Obtain 31 points in any suit before the other player does"),("war()",2,"Collect all of the cards"),("blackjack()","1+","Beat the dealer without going over 21 points"]
##print("List of games:\n")
##for game in games_list:
##    print("{}\n\tNumber of players: {}\n\tObject: {}".format(game[0],game[1],game[2]))
