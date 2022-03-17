from random import shuffle


VALUE_CARD = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
              "ten": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14}

NAME_CARD = ["two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "jack", "queen", "king", "ace"]

SIGN_CARD = ["hearts", "diamonds", "spades", "clubs"]

GAME_ON = True


class Player:

    def __init__(self, name):

        self.name = name
        self.cards_in_hand = []

    def remove_one(self):
        return self.cards_in_hand.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards_in_hand.extend(new_cards)
        else:
            self.cards_in_hand.append(new_cards)

    def __str__(self):
        return f"Player{self.name} has {len(self.cards_in_hand)}"


# Make a card class
class Card:

    def __init__(self, card_sign, card_name):
        self.card_sign = card_sign
        self.card_name = card_name
        self.value = VALUE_CARD[card_name]

    def __str__(self):
        return self.card_name + " of " + self.card_sign


# Make a deck
class Deck:

    def __init__(self):

        self.whole_deck = []

        for sign in SIGN_CARD:
            for name in NAME_CARD:
                # Create card object
                one_card = Card(sign, name)
                self.whole_deck.append(one_card)

    def shuffle(self):

        shuffle(self.whole_deck)

    def deal_one(self):
        return self.whole_deck.pop()


player_one = Player("one")
player_two = Player("two")

starting_deck = Deck()
starting_deck.shuffle()

for card in range(26):
    player_one.add_cards(starting_deck.deal_one())
    player_two.add_cards(starting_deck.deal_one())

while GAME_ON:

    if len(player_one.cards_in_hand) == 0:
        print("Player two wins")
        break

    if len(player_two.cards_in_hand) == 0:
        print("Player one wins")
        break

    player_one_hand = []
    player_one_hand.append(player_one.remove_one())

    player_two_hand = []
    player_two_hand.append(player_two.remove_one())

