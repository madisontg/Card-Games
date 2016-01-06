def thirty_one():
    # variables
    
    cards = Deck()
    cards.shuffle()
    player1 = []
    player2 = []
    discarded = None
    knock = False
    player = 1
    
    # populate hands
    for num in range(3):
        player1.append(cards.deal())
        player2.append(cards.deal())

    # clear screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")    

    # RUN "NORMAL" GAME
    while knock == False:
        
        # who goes?
        # player one goes
        if player == 1:
            print("--------------------------------------------------------------")
            
            # display cards
            print("PLAYER ONE\nYou have:")
            for card in player1:
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
                player1.append(new_card)
            else:
                if discarded != None:
                    new_card = discarded
                    player1.append(new_card)
                else:
                    print("Discard pile is empty.  Here is a card from the deck.")
                    new_card = cards.deal()
                    player1.append(new_card)
            # display new card
            print("New card:  {} {} {}".format(new_card[0],new_card[1],new_card[2]))
            
            # discard a card
            print("Which would you like to discard?")
            print("(a): {} {} {}".format(player1[0][0],player1[0][1],player1[0][2]))
            print("(b): {} {} {}".format(player1[1][0],player1[1][1],player1[1][2]))
            print("(c): {} {} {}".format(player1[2][0],player1[2][1],player1[2][2]))
            discard = input("(d): {} {} {}\n".format(player1[3][0],player1[3][1],player1[3][2]))
            if discard.lower().strip() == "a":
                discarded = player1.pop(0)
            elif discard.lower().strip() == "b":
                discarded = player1.pop(1)
            elif discard.lower().strip() == "c":
                discarded = player1.pop(2)
            elif discard.lower().strip() == "d":
                discarded = player1.pop(3)

            # display points in each suit
            print("Score:", find_score(player1))
            
            # knock?
            knock_ask = input("Would you like to knock? (y/n)\n")
            if knock_ask.lower().strip() == "y":
                knock = True # exists while loop
                player = 2

            # clear screen
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            
        # player two goes
        elif player == 2:
            print("--------------------------------------------------------------")
            
            # display cards
            print("PLAYER TWO\nYou have:")
            for tup in player1:
                print("         {} {} {}".format(tup[0],tup[1],tup[2]))
            if discarded == None:
                print("There is no discard.")
            else:
                print("Discard: {} {} {}".format(discarded[0],discarded[1],discarded[2]))
            print("PLAYER TWO:")
            
            # draw a new card
            deck_discard = input("Draw from (a)deck or (b)discard pile?\n")
            if deck_discard.lower().strip() == "a":
                new_card = cards.deal()
                player2.append(new_card)
            else:
                if discarded != None:
                    new_card = discarded
                    player2.append(new_card)
                else:
                    print("Discard pile is empty.  Here is a card from the deck.")
                    new_card = cards.deal()
                    player2.append(new_card)

            # display new card
            print("New card:  {} {} {}".format(new_card[0],new_card[1],new_card[2]))
            
            # discard a card
            print("Which would you like to discard?")
            print("(a): {} {} {}".format(player2[0][0],player2[0][1],player2[0][2]))
            print("(b): {} {} {}".format(player2[1][0],player2[1][1],player2[1][2]))
            print("(c): {} {} {}".format(player2[2][0],player2[2][1],player2[2][2]))
            discard = input("(d): {} {} {}\n".format(player2[3][0],player2[3][1],player2[3][2]))
            if discard.lower().strip() == "a":
                discarded = player2.pop(0)
            elif discard.lower().strip() == "b":
                discarded = player2.pop(1)
            elif discard.lower().strip() == "c":
                discarded = player2.pop(2)
            elif discard.lower().strip() == "d":
                discarded = player2.pop(3)

            # display points in each suit
            print("Score:", find_score(player2))
            
            # knock?
            knock_ask = input("Would you like to knock? (y/n)\n")
            if knock_ask.lower().strip() == "y":
                knock = True # exit while loop
                player = 1
            player = 1
            
            # clear screen
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            
    # RUN "KNOCKED" GAME
    # who goes
    # player two goes
    if player == 1:
        print("--------------------------------------------------------------")
        
        # display cards
        print("PLAYER ONE\nLAST TURN\nYou have:")
        for tup in player1:
            print("         {} {} {}".format(tup[0],tup[1],tup[2]))
        if discarded == None:
            print("There is no discard.")
        else:
            print("Discard: {} {} {}".format(discarded[0],discarded[1],discarded[2]))
        print("\nPLAYER ONE:")
        
        # draw a new card
        deck_discard = input("Draw from (a)deck or (d)discard pile?\n")
        if deck_discard.lower().strip() == "a":
            new_card = cards.deal()
            player1.append(new_card)
        else:
            if discarded != None:
                new_card = discarded
                player1.append(new_card)
            else:
                print("Discard pile is empty.  Here is a card from the deck.")
                new_card = cards.deal()
                player1.append(new_card)
        # display new card
        print("New card:  {} {} {}".format(new_card[0],new_card[1],new_card[2]))
        
        # discard a card
        print("Which would you like to discard?")
        print("(a): {} {} {}".format(player1[0][0],player1[0][1],player1[0][2]))
        print("(b): {} {} {}".format(player1[1][0],player1[1][1],player1[1][2]))
        print("(c): {} {} {}".format(player1[2][0],player1[2][1],player1[2][2]))
        discard = input("(d): {} {} {}\n".format(player1[3][0],player1[3][1],player1[3][2]))
        if discard.lower().strip() == "a":
            discarded = player1.pop(0)
        elif discard.lower().strip() == "b":
            discarded = player1.pop(1)
        elif discard.lower().strip() == "c":
            discarded = player1.pop(2)
        elif discard.lower().strip() == "d":
            discarded = player1.pop(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
    # player two goes    
    elif player == 2:
        print("--------------------------------------------------------------")
        # display cards
        print("PLAYER TWO\nLAST TURN.\nYou have:")
        for tup in player1:
            print("         {} {} {}".format(tup[0],tup[1],tup[2]))
        if discarded == None:
            print("There is no discard.")
        else:
            print("Discard: {} {} {}".format(discarded[0],discarded[1],discarded[2]))
        print("PLAYER TWO:")
            
        # draw a new card
        deck_discard = input("Draw from (a)deck or (b)discard pile?\n")
        if deck_discard.lower().strip() == "a":
            new_card = cards.deal()
            player2.append(new_card)
        else:
            if discarded != None:
                new_card = discarded
                player2.append(new_card)
            else:
                print("Discard pile is empty.  Here is a card from the deck.")
                new_card = cards.deal()
                player2.append(new_card)
        print("New card:  {} {} {}".format(new_card[0],new_card[1],new_card[2]))
        
        # discard a card
        print("Which would you like to discard?")
        print("(a): {} {} {}".format(player2[0][0],player2[0][1],player2[0][2]))
        print("(b): {} {} {}".format(player2[1][0],player2[1][1],player2[1][2]))
        print("(c): {} {} {}".format(player2[2][0],player2[2][1],player2[2][2]))
        discard = input("(d): {} {} {}\n".format(player2[3][0],player2[3][1],player2[3][2]))
        if discard.lower().strip() == "a":
            discarded = player2.pop(0)
        elif discard.lower().strip() == "b":
            discarded = player2.pop(1)
        elif discard.lower().strip() == "c":
            discarded = player2.pop(2)
        elif discard.lower().strip() == "d":
            discarded = player2.pop(3)

        # clear screen
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
    # GAME FINISHED; PRINT RESULTS
    print("Game over")
    first = max(find_score(player1).values())
    second = max(find_score(player2).values())
    print("Player 1 has ",first," points.",sep = "")
    print("Player 2 has ",second," points.", sep = "")
    if first < second:
        print("Player 2 won!")
    elif first > second:
        print("Player 1 won!")
    else:
        print("It was a tie!")
