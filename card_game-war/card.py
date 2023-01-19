try:
    from values import card_value
except Exception as e:
    print("#" * 25 + '\n')
    print("Import Error in file : card.py\n")
    print(e)


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_value[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


