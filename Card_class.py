class Card(object):
    
    suit_options = ["Hearts","Diamonds","Clubs","Spades"]
    value_options = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

    def __init__(self,int_value,suit):
        self.suit = suit
        self.value = int_value

    def __str__(self):
        card = [self.suit,self.value]
        #string = str(self.value) + " of " + (self.suit)
        return "{} of {}".format(self.suit,self.value)
        
    def set_suit(self,suit):
        self.suit = suit

    def set_value(self,int_value):
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
    

    def is_greater_than(self,other_card):
        if self.value > other_card.get_value():
            return True
        else:
            return False
