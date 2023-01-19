try:
    from values import suits, card_value, ranks
    from player import Player
    from deck import Deck
    from card import Card
except Exception as e:
    print("#" * 25 + '\n')
    print("Import Error in file : main.py\n")
    print(e)

player_one = Player('One')
player_two = Player('Two')
new_deck = Deck()
new_deck.shuffle()

for card in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())
game_on = True
round_number = 0
while game_on:

    round_number = round_number + 1
    print("Round : {}\n".format(round_number))

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two Wins.")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins.")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)
            at_war = False
        else:
            print("WAR !! \n")
            if len(player_one.all_cards) < 3:
                print("Player One cannot declare WAR.\n")
                print("Player Two WINS !!\n")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player Two cannot declare WAR.\n")
                print("Player One WINS !!\n")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
