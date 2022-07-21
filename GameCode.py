
from random import shuffle

class Card :

    suits = {" ", "Red", "Green", "Blue", "Yellow", "Trump"}

    values = {"Switch", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"}

    def __init__(self, suit, value) :
        self.suit = suit
        self.value = value

    def show(self):
        print ("The {} of {}".format(self.value, self.suit))

class Deck :

    def __init__(self) :
        self.cards = []
        for suit in ["Red", "Green", "Blue", "Yellow"] :
            for value in range(1, 16) :
                self.cards.append(Card(suit, value))
        for value in range(1,9) :
            self.cards.append(Card("Trump", value))
        for i in range(0, 4) :
            self.cards.append(Card(" ", "Switch"))
        shuffle(self.cards)

    def show(self) :
        for card in self.cards :
            card.show()

    def shuffle(self) :
        import random
        random.shuffle(self.cards)

    def drawCard(self) :
        return self.cards.pop()

    def drawCards(self, n) :
        cards = []
        for i in range(0, n) :
            cards.append(self.drawCard())
        return cards

class Player :

    def __init__(self, name) :
        self.name = name
        self.hand = []
        self.score = 0

    def draw(self, deck) :
        self.hand.append(deck.drawCard())

    def drawCards(self, deck, n) :
        for i in range(0, n) :
            self.draw(deck)
    
    def showHand(self) :
        for card in self.hand :
            card.show()

    def playCard(self, card) :
        self.hand.remove(card)
        return card.value

    def showScore(self) :
        print ("{} has {} points".format(self.name, self.score))

class Game :

    def __init__(self) :
        self.deck = Deck()
        self.players = []
        self.turn = 0s
        
    def addPlayer(self, player) :
        self.players.append(player)
    
    def play(self) :

        if len(self.players) == 0 :
            print("There are no players") # How can you play a game without players?
        elif len(self.players) == 1 :
            print("There is only one player") # How can you play a game with only one player?
        elif len(self.players) == 2 :
            print("There are two players, 20 cards are removed") # 20 cards are removed from the deck when there are only two players
            self.deck.drawCards(20)
            num_cards_pp = 13
        elif len(self.players) == 3 :
            print("There are three players") # No cards are removed from the deck when there are three players - each player receives 12 cards
            num_cards_pp = 12
        elif len(self.players) == 4 :
            print("There are four players") # No cards are removed from the deck when there are four players - each player receives 9 cards
            num_cards_pp = 9
        elif len(self.players) == 5 :
            print("There are five players") # 2 cards are removed from the deck when there are five players - each player receives 7 cards
            num_cards_pp = 7
        elif len(self.players) == 6 :
            print("There are six players") # No cards are removed from the deck when there are six players - each player receives 6 cards
            num_cards_pp = 6
        else : 
            print("There are more than six players") # The limit on the number of players is six

        for player in self.players : # Each player draws cards from the deck until they have the right number of cards
            player.drawCards(self.deck, num_cards_pp)



