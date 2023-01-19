
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return "Player {} has {} cards.\n".format(self.name, len(self.all_cards))

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)



