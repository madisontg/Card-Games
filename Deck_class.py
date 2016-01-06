class Deck(object):
    import random
    list_of_cards = []
    
    while len(list_of_cards) <= 52:
        card = Card(Card.value_options[random.randint(0,12)],Card.suit_options[random.randint(0,3)])
        
        if card not in list_of_cards:
            list_of_cards.append(card)
            
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

    def empty():
        if len(list_of_cards) == 0:
            return True
        else:
            return False
        
