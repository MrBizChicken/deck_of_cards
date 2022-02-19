import random
class Card:
    def __init__(self, suite, vaule):
        self.suite = suite
        self.vaule = vaule



    def get_card_vaule(self):
        return (self.suite, self.vaule)



class Cards:
    def __init__(self):
        self.suite = ["Heart", "Diamond", "Club", "Spade"]
        self.vaule = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.deck = []
        self.discard_pile = []




    def make_deck(self):
        self.deck = []

        for s in range(len(self.suite)):
            for v in range(len(self.vaule)):
                card = Card(self.vaule[v], self.suite[s])
                self.deck.append(card)


    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck



    def deal(self, players, num_to_deal):
        hands = []

        for i in range(players):
            hands.append([])

        for ntd in range(num_to_deal):
            for player in range(players):
                hands[player].append(self.draw(1))

        return hands



    def draw(self, ammount):
        hand = []

        for i in range(ammount):
            hand.append(self.deck.pop())

        return hand



    def discard(self, cards):
        for i in range(cards):
            self.discard_pile.append(self.deck.pop(0))
        return self.discard_pile



    def mix_discard(self):
        if self.deck == []:
            self.deck = self.discard_pile
            return self.deck

    def show_deck(self):
        for x in range(len(self.deck)):
            print(self.deck[x])


cards = Cards()
cards.make_deck()
cards.shuffle_deck()
cards.discard(52)
cards.mix_discard()
cards.show_deck()
cards.deal(2)


def show_hand(cards):
    for card in cards:
        print(card.get_card_vaule())

hnd = cards.deal(2, 3)

for h in hnd:
    for c in h:
        show_hand(c)

def show_discard(cards):
    for card in cards:
        print(card.get_card_vaule())

dis = cards.discard(4)

for c in dis:
    show_hand(c)







cards.draw()
