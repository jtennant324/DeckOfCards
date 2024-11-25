#Jessica Tennant
#CIS261
#Week 8 Lab Deck of Cards

import random


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in Deck.suits for rank in Deck.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)
        print("\nI have shuffled a deck of 52 cards.")

    def deal(self, num_cards):
        if num_cards > len(self.deck):
            raise ValueError("Not enough cards left in the deck to deal that many.")
        dealt_cards = self.deck[:num_cards]
        self.deck = self.deck[num_cards:]
        return dealt_cards

    def cards_remaining(self):
        return len(self.deck)


def main():
    print("Card Dealer")

    while True:
        deck = Deck()

        while True:
            try:
                num_cards = int(input("\nHow many cards would you like?: "))
                if num_cards < 1:
                    print("Please enter a valid number of cards.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            try:
                dealt_cards = deck.deal(num_cards)
                print("\nHere are your cards:")
                for card in dealt_cards:
                    print(card)

                print(f"\nThere are {deck.cards_remaining()} cards left in the deck.")
            except ValueError as e:
                print(f"Error: {e}")

            print("\nGood luck!")
            input("Press any key to continue . . . ")

            if deck.cards_remaining() == 0:
                print("\nNo cards remaining. Good game!")
                break

        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            input("Press any key to continue . . . ")
            break


if __name__ == "__main__":
    main()

