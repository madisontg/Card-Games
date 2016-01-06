def find_hand_value(player):
    value = 0
    for card in players(player):
        temp = card.get_value()
        if isinstance(temp,int):
            value += temp
        elif temp == "Jack" or temp == "Queen" or temp == "King":
            value += 10
        elif temp == "Ace":
            if value < 10:
                value += 11
            else:
                value += 1

    return value

def blackjack():
    # establish deck
    cards = Deck()
    cards.shuffle()
    
    # establish player hands and dealer hand
    hands = []
    dealer = []
    num = int(input("How many players?\n"))
    for player in range(num):
        hands.append([])
    for player in hands:
        player.append(cards.deal())
    dealer.append(cards.deal())
    for player in hands:
        player.append(cards.deal())
    dealer.append(cards.deal())

    # print all player cards (by player) and first dealer card


    # each player gets a turn
    for player in hands:
        inputted = "Yes"
        for player in hands:
            print("Player {}: {} and {}".format(index(player) + 1, player[0], player[1]))
            print("Dealer card: {}".format(dealer[0]))
            print("PLAYER {}".format(index(player) + 1))
            while inputted != "stand":
                inputted = input("Hit or stand?\n").lower().strip()  
                # if hit, draw one card
                if inputted == "Hit":
                    player.append(cards.deal())
                # if hand value > 21 print busted
                if find_hand_value(player) > 21:
                    print("Busted")
                    
                        
            print("_____________________________________________________________________\n")

    # dealer goes
    while find_hand_value(dealer) < 17:
        dealer.append(cards.deal())
        if find_hand_value(dealer) > 21:
            print("Dealer busts")
            for player in hands:
                if find_hand_value(player) <= 21:
                    print("Player {}, with {}, wins!".format(index(player) + 1, find_hand_value(player)))
            else:
                print("Player {} busted too.".format(index(player) + 1))
        return None

    # return scores, who won
    for player in hands:
        if find_hand_value(player) <= 21:
            if find_hand_value(player) > find_hand_value(dealer):
                print("Player {}, with {}, wins!".format(index(player) + 1, find_hand_value(player)))
            else:
                print("Player {} finished with {}".format(index(player) + 1, find_hand_value(player)))
        else:
            print("Player {} busted with {}".format(index(player) + 1), find_hand_value(player))
             
