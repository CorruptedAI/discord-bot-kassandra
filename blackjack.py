import random
import os


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

    print('\t   |Balance: $' + str(money))
     
     
    # For better control over bets
    def place_bet():
        global bet
        bet = input('\t   |Your bet: $')
    place_bet()
     
     
    while True:
        try:
            int(bet)
        except ValueError:
            place_bet()
        if int(bet) <= 0:
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
    def calculate(arr):
    
        scoresult = []
        for cat in arr:
            scoresult.append(all_cards.get(cat))
            
        result = 0
        for element in scoresult:
            result += element
            
        if result > 21:
            all_cards["|A|♣"] = 1
            all_cards["|A|♦"] = 1
            all_cards["|A|♥"] = 1
            all_cards["|A|♠"] = 1
        elif result < 11:
            all_cards["|A|♣"] = 11
            all_cards["|A|♦"] = 11
            all_cards["|A|♥"] = 11
            all_cards["|A|♠"] = 11
                
        scoresult = []
        for cat in arr:
            scoresult.append(all_cards.get(cat))
            
        result = 0
        for element in scoresult:
            result += element
            
        return result
        
        
    # Proposal to restart the game after its completion
    def reset_game():
    
        if money <= 0:
            exit()
    
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
        player.append(card1)
        cards.remove(card1)
        
        card2 = random.choice(cards)
        player.append(card2)
        cards.remove(card2)
        
        print('\n\t   Your cards: ' + card1 + ' and ' + card2)
        
        if all_cards.get(card1) == 1 and all_cards.get(card2) == 10 or all_cards.get(card1) == 10 and all_cards.get(card2) == 1:
            print('\n\t   ----------------\n\t   ---BLACKJACK!---\n\t   ----------------\n\t   --->YOU WIN!<---')
            
            money += round(int(bet) * 1.5)
            print('\t   |Balance: $' + str(money))
            
            reset_game()


    # Settings for the dealer
    def start_dealer():
    
        global money
        
        card3 = random.choice(cards)
        dealer.append(card3)
        cards.remove(card3)
        
        card4 = random.choice(cards)
        dealer.append(card4)
        cards.remove(card4)

        if all_cards.get(card3) == 1 and all_cards.get(card4) == 10 or all_cards.get(card3) == 10 and all_cards.get(card4) == 1:
            print('\t   Dealer cards: ' + card3 + ' and ' + card4)
            print('\n\t   ----------------\n\t   ---BLACKJACK!---\n\t   ----------------\n\t   --->YOU LOSE<---')
            
            money -= round(int(bet) * 1.5)
            print('\t   |Balance: $' + str(money))
            
            reset_game()
            
        print('\t   Dealer cards: ' + card3 + ' and |?|')
            
            
    # AI of the dealer
    def give_card_dealer():
        
        while calculate(dealer) < 17:
            card_hit_dealer = random.choice(cards)
            dealer.append(card_hit_dealer)
            cards.remove(card_hit_dealer)
            print('\t   and ' + card_hit_dealer)
            
            
    # Request for issuing an additional card
    def give_card():
    
        global money
        
        push = ''
        for stack in dealer:
            push += stack + ' '
    
        if calculate(dealer) > 21:
            print('\n\t   Dealer cards: ' + push + '\n\t   Dealer score: ' + str(calculate(dealer)) + '\n\n\t   --->YOU WIN!<---')
            
            money += int(bet)
            print('\t   |Balance: $' + str(money))
            
            reset_game()
                
        if calculate(player) == 21:
            hit = 'n'
        else:
            hit = input('\n\t\tHit me? (y/n)\n')
            
        if hit == 'y':
            card_hit = random.choice(cards)
            player.append(card_hit)
            cards.remove(card_hit)
            
            print('\t   New card: ' + card_hit)
            print('\t   Your score: ' + str(calculate(player)))
            
            if calculate(player) > 21:
                print('\n\t   Dealer cards: ' + push + '\n\t   Dealer score: ' + str(calculate(dealer)) + '\n\n\t   --->YOU LOSE<---')
                
                money -= int(bet)
                print('\t   |Balance: $' + str(money))
                
                reset_game()
                
            give_card()

        elif hit == 'n':
            
            if calculate(player) > calculate(dealer):
                print('\n\t   Dealer cards: ' + push + '\n\t   Dealer score: ' + str(calculate(dealer)) + '\n\n\t   --->YOU WIN!<---')
                
                money += int(bet)
                print('\t   |Balance: $' + str(money))
                
                reset_game()
                
            elif calculate(player) < calculate(dealer):
                print('\n\t   Dealer cards: ' + push + '\n\t   Dealer score: ' + str(calculate(dealer)) + '\n\n\t   --->YOU LOSE<---')
                
                money -= int(bet)
                print('\t   |Balance: $' + str(money))
                
                reset_game()
                
            elif calculate(player) == calculate(player):
                print('\n\t   Dealer cards: ' + push + '\n\t   Dealer score: ' + str(calculate(dealer)) + '\n\n\t   ---->PUSH<----')
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