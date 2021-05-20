import random
from art import logo
from replit import clear


cards = [11, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play_game = "y"
while play_game == "y":
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    print(logo)
    if play_game == "n":
        break
    user_cards = []
    comp_cards = []

    #user selection
    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    user_cards.append(user_card1)
    user_cards.append(user_card2)
    user_current_score = user_card1 + user_card2
    print(f"Your cards: {user_cards}  Current score: {user_current_score}")

    #computer selection
    comp_card1 = random.choice(cards)
    comp_card2 = random.choice(cards)
    comp_cards.append(comp_card1)
    comp_cards.append(comp_card2)
    print(f"Computer's first card: {comp_card1}")
    comp_current_score = comp_card1 + comp_card2

    #function for adding values of cards:
    def user_score_calc(card_value):
        return user_current_score + card_value
    def comp_score_calc(card_value):
        return comp_current_score + card_value

    #lose or win definition
    def lose():
        print("You lose")
        print(f"computer final hand: {comp_cards},  final score: {comp_current_score}")
    def win():
        print("You win")
        print(f"computer final hand: {comp_cards},  final score: {comp_current_score}")

    #Ace logic
    def ace_value_user():
        if user_current_score > 21:
            cards[0] = 1
    def ace_value_comp():
        if user_current_score > 21:
            cards[0] = 1

    #loop start
    game_continue = True
    while game_continue:
        ask_user = input("Type 'y' for hit , 'n' for stand: ")
        if ask_user == "y":
            user_card3 = random.choice(cards)
            user_cards.append(user_card3)
            user_current_score = user_score_calc(user_card3)
            print(f"Your cards: {user_cards}  Current score: {user_current_score}")
            #hit again
            if user_current_score < 21:
                continue
            elif user_current_score > 21:
                lose()
                game_continue = False
            
            
        elif ask_user == "n":
            while comp_current_score < 17:
                comp_card3 = random.choice(cards)
                comp_cards.append(comp_card3)
                comp_current_score =  comp_score_calc(comp_card3)
            if user_current_score == comp_current_score:
                print("Draw")
                print(f"computer final hand: {comp_cards},  final score: {comp_current_score}")
                game_continue = False
            elif comp_current_score == 21:
                lose()
                game_continue = False
            elif user_current_score == 21:
                win()
                game_continue = False
            elif user_current_score <= 21 and (comp_current_score > 21 or user_current_score > comp_current_score):
                win()
                game_continue = False
            elif (user_current_score > 21 or comp_current_score > user_current_score) and comp_current_score <= 21:
                lose()
                game_continue = False
            elif user_current_score > 21:
                lose()
                game_continue = False
            elif comp_current_score > 21:
                win()
                game_continue = False

            

    # todo 1: Add hit again option ✔️
    # todo 2: counting ace as 11
    # todo 3: dealer/computer passive(not appending random values) until we stand ✔️
    # todo 4: Looping the whole game to play again and again✔️
    # todo 5: AI when user says no ✔️
