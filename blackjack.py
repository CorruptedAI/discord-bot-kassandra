import random


all_cards = {
    "|2|♣": 2, "|2|♦": 2, "|2|♥": 2, "|2|♠": 2,
    "|3|♣": 3, "|3|♦": 3, "|3|♥": 3, "|3|♠": 3,
    "|4|♣": 4, "|4|♦": 4, "|4|♥": 4, "|4|♠": 4,
    "|5|♣": 5, "|5|♦": 5, "|5|♥": 5, "|5|♠": 5,
    "|6|♣": 6, "|6|♦": 6, "|6|♥": 6, "|6|♠": 6,
    "|7|♣": 7, "|7|♦": 7, "|7|♥": 7, "|7|♠": 7,
    "|8|♣": 8, "|8|♦": 8, "|8|♥": 8, "|8|♠": 8,
    "|9|♣": 9, "|9|♦": 9, "|9|♥": 9, "|9|♠": 9,
    "|10|♣": 10, "|10|♦": 10, "|10|♥": 10, "|10|♠": 10,
    "|J|♣": 10, "|J|♦": 10, "|J|♥": 10, "|J|♠": 10,
    "|Q|♣": 10, "|Q|♦": 10, "|Q|♥": 10, "|Q|♠": 10,
    "|K|♣": 10, "|K|♦": 10, "|K|♥": 10, "|K|♠": 10,
    "|A|♣": 1, "|A|♦": 1, "|A|♥": 1, "|A|♠": 1
}
         

cards = []
for card in all_cards:
  cards.append(card)


# Main function, launches all game processes
def run_game():
    
    player = []
    dealer = []
    

    # Calculates the amount of points for the player
    def calc_score(name):
        result = 0
        for element in name:
            result += element
        return result
        
        
    # Proposal to restart the game after its completion
    def reset_game():
        reset = input("\n\n\t\tPlay again? (y/n)\n")
        if reset == "y":
            run_game()
        if reset == "n":
            exit()
        

    # Settings for the player
    def start_player():
        
        card1 = random.choice(cards)
        card2 = random.choice(cards)
    
        card1_var = all_cards.get(card1)
        card2_var = all_cards.get(card2)

        if int(calc_score(player)) < 12:
            all_cards["|A|♣"] = 10
            all_cards["|A|♦"] = 10
            all_cards["|A|♥"] = 10
            all_cards["|A|♠"] = 10
        for card in all_cards:
            cards.append(card)
            
        player.append(card1_var)
        player.append(card2_var)
        
        print("\t   Your cards: " + card1 + " and " + card2)
        
        if card1_var == 1 and card2_var == 10 or card1_var == 10 and card2_var == 1:
            print("\t----------------\n\t---BLACKJACK!---\n\t----------------\n\t--->YOU WIN!<---")
            reset_game()
                    
        print("\t   score: " + str(calc_score(player)))


    # Settings for the dealer
    def start_dealer():
        card3 = random.choice(cards)
        card4 = random.choice(cards)
    
        card3_var = all_cards.get(card3)
        card4_var = all_cards.get(card4)
    
        dealer.append(card3_var)
        dealer.append(card4_var)
      
        print("\t   Dealer cards: " + card3 + " and |?|")
        
        if card3_var == 1 and card4_var == 10 or card3_var == 10 and card4_var == 1:
            print("\t----------------\n\t---BLACKJACK!---\n\t----------------\n\t--->YOU LOSE<---")
            reset_game()
                
        print("\t   score: |?|")
            
            
    # Artificial Intelligence Dealer
    def give_card_dealer():
        if int(calc_score(dealer)) < 12:
            all_cards["|A|♣"] = 10
            all_cards["|A|♦"] = 10
            all_cards["|A|♥"] = 10
            all_cards["|A|♠"] = 10
        for card in all_cards:
            cards.append(card)
        card_hit_dealer = random.choice(cards)
        card_hit_dealer_rev = all_cards.get(card_hit_dealer)
    give_card_dealer()
           
           
    # Request for issuing an additional card
    def give_card():
        hit = input("\n\t\tHit? (y/n)\n")
        if hit == "y":
            if int(calc_score(player)) >= 12:
                all_cards["|A|♣"] = 1
                all_cards["|A|♦"] = 1
                all_cards["|A|♥"] = 1
                all_cards["|A|♠"] = 1
            for card in all_cards:
                cards.append(card)
            card_hit = random.choice(cards)
            card_hit_rev = all_cards.get(card_hit)
            player.append(card_hit_rev)
            print("\t   Hit: " + card_hit)
            print("\t   score: " + str(calc_score(player)))
            if int(calc_score(player)) > 21:
                print("\t--->YOU LOSE<---")
                reset_game()
                
            give_card()

        elif hit == "n":
            if int(calc_score(player)) > int(calc_score(dealer)):
                print("\t--->YOU WIN!<---")
                reset_game()
            elif int(calc_score(player)) < int(calc_score(dealer)):
                print("\t   Dealer score: " + str(calc_score(dealer)) + "\n\t--->YOU LOSE<---")
                reset_game()
            elif int(calc_score(player)) == int(calc_score(dealer)):
                print("\t--->DRAW<---")
                reset_game()


    start_player()
    start_dealer()
    give_card()


start = input("\n\t\tStart the game? (y/n)\n")
if start == "y":
    run_game()
elif start == "n":
    exit()