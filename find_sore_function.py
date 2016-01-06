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

    return "Hearts: {}, Diamonds: {}, Clubs: {}, Spades: {}".format(hearts,diamonds,clubs,spades)
