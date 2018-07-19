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


# Main function, launches all game processes
def run_game():
    
    player = []
    dealer = []
    
    copy_cards = all_cards.copy()
    
    cards = []
    for card in copy_cards:
        cards.append(card)
        

    # Calculates the amount of points for the player
    def calc_score(name):
        result = 0
        for element in name:
            result += element
        return result
        
        
    # Proposal to restart the game after its completion
    def reset_game():
        reset = input('\n\n\t\tPlay again? (y/n)\n')
        if reset == 'y':
            run_game()
        if reset == 'n':
            exit()
        

    # Settings for the player
    def start_player():
        
        card1 = random.choice(cards)
        card1_var = copy_cards.get(card1)
        del copy_cards[card1]
        cards.remove(card1)
        
        card2 = random.choice(cards)
        card2_var = copy_cards.get(card2)
        del copy_cards[card2]
        cards.remove(card2)
        
        player.append(card1_var)
        player.append(card2_var)
        
        print('\t   Your cards: ' + card1 + ' and ' + card2)
        
        if card1_var == 1 and card2_var == 10 or card1_var == 10 and card2_var == 1:
            print('\t----------------\n\t---BLACKJACK!---\n\t----------------\n\t--->YOU WIN!<---')
            reset_game()
                    
        print('\t   score: ' + str(calc_score(player)))


    # Settings for the dealer
    def start_dealer():
        card3 = random.choice(cards)
        card3_var = copy_cards.get(card3)
        del copy_cards[card3]
        cards.remove(card3)
        
        card4 = random.choice(cards)
        card4_var = copy_cards.get(card4)
        del copy_cards[card4]
        cards.remove(card4)
    
        dealer.append(card3_var)
        dealer.append(card4_var)
      
        print('\t   Dealer cards: ' + card3 + ' and |?|')
        
        if card3_var == 1 and card4_var == 10 or card3_var == 10 and card4_var == 1:
            print('\t----------------\n\t---BLACKJACK!---\n\t----------------\n\t--->YOU LOSE<---')
            reset_game()
                
        print('\t   score: |?|')
            
            
    # Artificial intelligence of the dealer
    def give_card_dealer():
        
        if calc_score(dealer) < 11:
            copy_cards["|A|♣"] = 11
            copy_cards["|A|♦"] = 11
            copy_cards["|A|♥"] = 11
            copy_cards["|A|♠"] = 11
            
            card_hit_dealer = random.choice(cards)
            card_hit_dealer_var = copy_cards.get(card_hit_dealer)
            del copy_cards[card_hit_dealer]
            cards.remove(card_hit_dealer)
            
            dealer.append(card_hit_dealer_var)
            
        elif calc_score(dealer) < 17:
            probability = [0, 1, 2]
            percent33 = random.choice(probability)
            
            copy_cards["|A|♣"] = 1
            copy_cards["|A|♦"] = 1
            copy_cards["|A|♥"] = 1
            copy_cards["|A|♠"] = 1
                
            if percent33 == 1:
                card_hit_dealer = random.choice(cards)
                card_hit_dealer_var = copy_cards.get(card_hit_dealer)
                del copy_cards[card_hit_dealer]
                cards.remove(card_hit_dealer)
                
                dealer.append(card_hit_dealer_var)
                
           
    # Request for issuing an additional card
    def give_card():
        if calc_score(dealer) > 21:
            print('\t--->YOU WIN<---')
            reset_game()
            
        hit = input('\n\t\tHit? (y/n)\n')
            
        if hit == 'y':
            if calc_score(player) <= 11:
                copy_cards["|A|♣"] = 11
                copy_cards["|A|♦"] = 11
                copy_cards["|A|♥"] = 11
                copy_cards["|A|♠"] = 11
            else:
                copy_cards["|A|♣"] = 1
                copy_cards["|A|♦"] = 1
                copy_cards["|A|♥"] = 1
                copy_cards["|A|♠"] = 1
                
            card_hit = random.choice(cards)
            card_hit_rev = copy_cards.get(card_hit)
            del copy_cards[card_hit]
            cards.remove(card_hit)
            
            player.append(card_hit_rev)
            
            print('\t   Hit: ' + card_hit)
            print('\t   score: ' + str(calc_score(player)))
            
            if calc_score(player) > 21:
                print('\t--->YOU LOSE<---')
                reset_game()
                
            give_card()

        elif hit == 'n':
            if calc_score(player) > calc_score(dealer):
                print('\t--->YOU WIN!<---')
                reset_game()
                
            elif calc_score(player) < calc_score(dealer):
                print('\t   Dealer score: ' + str(calc_score(dealer)) + '\n\t--->YOU LOSE<---')
                reset_game()
                
            elif calc_score(player) == calc_score(dealer):
                print('\t--->DRAW<---')
                reset_game()


    start_player()
    start_dealer()
    give_card_dealer()
    give_card()


start = input('\n\t\tStart the game? (y/n)\n')
if start == 'y':
    run_game()
elif start == 'n':
    exit()