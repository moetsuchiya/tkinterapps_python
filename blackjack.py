import random
suits = ['♥', '♦', '♣', '♠']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
cards = [f'{suit}{number}' for suit in suits for number in numbers]
random.shuffle(cards)
dealer_cards = [cards.pop() for _ in range(2)]
player_cards = [cards.pop() for _ in range(2)]


"""
def stand():
    print(your_cards)
    print(dealer_cards)"""

