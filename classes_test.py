class SimpleCard(object):
    value_options = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return "{}".format(self.value)

    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def is_greater_than(self,other):
        try: # are they comparable (both of type int)
            if int(self.value) > int(other.value):
                return True
            else:
                return False
        except ValueError: # they are not both ints
            # find value of card
            if self.value == "Jack" or self.value == "Queen" or self.value == "King":
                self_value = 10
            elif self.value == "Ace":
                self_value = 11
            else:
                self_value = self.value
            # find value of other card
            if other.value == "Jack" or other.value == "Queen" or other.value == "King":
                other_value = 10
            elif other.value == "Ace":
                other_value = 11
            else:
                other_value = other.value
            # compare values for return, return
            if self_value > other_value:
                return True
            else:
                return False
            
class Card(SimpleCard):
    
    suit_options = ["Hearts","Diamonds","Clubs","Spades"]

    def __init__(self,value,suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value,self.suit)
        
    def set_suit(self,suit):
        self.suit = suit

    def get_suit(self):
        return self.suit
    
class Deck(object):
    import random
    list_of_cards = []

    def __init__(self):
        for suit in Card.suit_options:
            for value in SimpleCard.value_options:
                card = Card(value,suit)
                self.list_of_cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.list_of_cards)

    def deal(self):
        return self.list_of_cards.pop()
    
    def __str__(self):        
        print("In this deck:")
        for card in self.list_of_cards:
            print(card)
        return ("")

    def __repr__(self):
        return self.__str__()

    def empty():
        if len(list_of_cards) == 0:
            return True
        else:
            return False
 
class SimpleDeck(Deck):
    import random
    list_of_cards = []

    def __init__(self):
        for suit in range(4):
            for value in SimpleCard.value_options:
                card = SimpleCard(value)
                self.list_of_cards.append(card)

def simple_war():
    pass

def full_war():
    cards = Deck()
    cards.shuffle()
    assert isinstance(cards,Deck)
    player1 = []
    player2 = []
    for num in range(26):
        player1.append(cards.deal())
        player2.append(cards.deal())
    total = 52
        
    while len(player1) > 0 and len(player2) > 0 and total == 52:
        print("Player 1 number of cards:", len(player1))
        print("Player 2 number of cards:", len(player1))
        print("---------------------------")
        
        p1card = player1.pop(0)
        p2card = player2.pop(0)
        print("Player 1:", p1card)
        print("Player 2:", p2card)
        print("\n")
        
        if p1card.is_greater_than(p2card):
            print("Player 1 gets the cards.")
            player1.append(p1card)
            player1.append(p2card)
            print("cards transferred")
            
        elif p2card.is_greater_than(p1card):
            print("Player 2 gets the cards.")
            player2.append(p1card)
            player2.append(p2card)
            print("cards transferred")
            
        elif p2card.get_value == p1card.get_value:
            its_war(player1,player2,p1card,p2card) 
        total = len(player1) + len(player2)

    if len(player1) == 0:
        print("Player 1 won!")
    elif len(player2) == 0:
        print("Player 2 won!")
    else:
        print(total)

def its_war(one, two, card1, card2):
    print("It's war")
    facedowns = []
    facedowns.append(card1)
    facedowns.append(card2)
    # does player 1 have enough cards for a war
    if len(one) > 2:
        facedowns.append(one.pop(0))
        facedowns.append(one.pop(0))
        ante1 = one.pop(0)
    else: # pity-win
        print("Player 1 gets the cards by default")
    # does player 2 have enough cards for a war
    if len(two) > 2:
        facedowns.append(two.pop(0))
        facedowns.append(two.pop(0))
        ante2 = two.pop(0)
    else: # pity-win
        print("Player 2 gets the cards by default")
    # commence war
    if ante1.is_greater_than(ante2):
        print("Player 1 gets the cards")
        for card in facedowns:
            one.append(card)
            print("cards transferred")
    elif ante2.is_greater_than(ante1):
        print("Player 2 gets the cards")
        for card in facedowns:
            two.append(card)
            print("cards transferred")
    elif ante1 == ante2:
        its_war(one,two,ante1,ante2)
full_war()
