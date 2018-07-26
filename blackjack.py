import random
import os


"""Because of the complexity of the implementation,
   |A| will always be static"""
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

money = 500


# Main function, launches all game processes
def run_game():
    if money <= 0:
        print('\t   |Balance: $' + str(money))
        print('\t   |Insufficient funds')
        exit()
     
    print('\t   |Balance: $' + str(money))
     
     
    # For int(bet)ter control over int(bet)s
    def place_bet():
        global bet
        bet = input('\t   |Your bet: ')
    place_bet()
     
    while True:
        try:
            int(bet)
        except ValueError:
            place_bet()
        else:
            break
     
    if int(bet) > money:
        place_bet()
    
    player = []
    dealer = []
    
    cards = []
    for card in all_cards:
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
            os.system('clear')
            run_game()
        if reset == 'n':
            exit()
        

    # Settings for the player
    def start_player():
        global money
        
        card1 = random.choice(cards)
        card1_var = all_cards.get(card1)
        cards.remove(card1)
        
        card2 = random.choice(cards)
        card2_var = all_cards.get(card2)
        cards.remove(card2)
        
        player.append(card1_var)
        player.append(card2_var)
        
        print('\n\t   Your cards: ' + card1 + ' and ' + card2)
        
        if card1_var == 1 and card2_var == 10 or card1_var == 10 and card2_var == 1:
            print('\n\t   ----------------\n\t   ---BLACKJACK!---\n\t   ----------------\n\t   --->YOU WIN!<---')
            
            money += round(int(bet) * 1.5)
            print('\t   |Balance: $' + str(money))
            
            reset_game()
                    
        print('\t   score: ' + str(calc_score(player)))


    # Settings for the dealer
    def start_dealer():
        global money
        
        card3 = random.choice(cards)
        card3_var = all_cards.get(card3)
        cards.remove(card3)
        
        card4 = random.choice(cards)
        card4_var = all_cards.get(card4)
        cards.remove(card4)
    
        dealer.append(card3_var)
        dealer.append(card4_var)
      
        
        if card3_var == 1 and card4_var == 10 or card3_var == 10 and card4_var == 1:
            print('\t   Dealer cards: ' + card3 + ' and ' + card4)
            print('\n\t   ----------------\n\t   ---BLACKJACK!---\n\t   ----------------\n\t   --->YOU LOSE<---')
            
            money -= round(int(bet) * 1.5)
            print('\t   |Balance: $' + str(money))
            
            reset_game()
        print('\t   Dealer cards: ' + card3 + ' and |?|')
            
            
    # Artificial intelligence of the dealer
    def give_card_dealer():
        while calc_score(dealer) < 17:
            card_hit_dealer = random.choice(cards)
            card_hit_dealer_var = all_cards.get(card_hit_dealer)
            cards.remove(card_hit_dealer)
            print('\t   and ' + card_hit_dealer)
            
            dealer.append(card_hit_dealer_var)
                
           
    # Request for issuing an additional card
    def give_card():
        global money
    
        if calc_score(dealer) > 21:
            print('\n\t   Dealer score: ' + str(calc_score(dealer)) + '\n\n\t   --->YOU WIN!<---')
            
            money += int(bet)
            print('\t   |Balance: $' + str(money))
            
            reset_game()
            
        if calc_score(player) == 21:
            hit = 'n'
        else:
            hit = input('\n\t\tHit me? (y/n)\n')
            
        if hit == 'y':
            card_hit = random.choice(cards)
            card_hit_rev = all_cards.get(card_hit)
            cards.remove(card_hit)
            
            player.append(card_hit_rev)
            
            print('\t   Hit card: ' + card_hit)
            print('\t   Your score: ' + str(calc_score(player)))
            
            if calc_score(player) > 21:
                print('\t   Dealer score: ' + str(calc_score(dealer)) + '\n\n\t   --->YOU LOSE<---')
                
                money -= int(bet)
                print('\t   |Balance: $' + str(money))
                
                reset_game()
                
            give_card()

        elif hit == 'n':
            if calc_score(player) > calc_score(dealer):
                print('\t   Dealer score: ' + str(calc_score(dealer)) + '\n\n\t   --->YOU WIN!<---')
                
                money += int(bet)
                print('\t   |Balance: $' + str(money))
                
                reset_game()
                
            elif calc_score(player) < calc_score(dealer):
                print('\t   Dealer score: ' + str(calc_score(dealer)) + '\n\n\t   --->YOU LOSE<---')
                
                money -= int(bet)
                print('\t   |Balance: $' + str(money))
                
                reset_game()
                
            elif calc_score(player) == calc_score(dealer):
                print('\t   Dealer score: ' + str(calc_score(dealer)) + '\n\n\t   --->PUSH<---')
                print('\t   |Balance: $' + str(money))
                
                reset_game()


    start_player()
    start_dealer()
    give_card_dealer()
    give_card()


os.system('clear')
start = input('\t\tStart the game? (y/n)\n')
if start == 'y':
    os.system('clear')
    run_game()
elif start == 'n':
    exit()