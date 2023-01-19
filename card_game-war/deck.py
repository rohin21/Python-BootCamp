
try:
    import values
    from random import shuffle
    from card import Card
except Exception as e:
    print("#" * 25 + '\n')
    print("Import Error in file : deck.py\n")
    print(e)


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in values.suits:
            for rank in values.ranks:

                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
