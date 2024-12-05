import random
suits = ['♥', '♦', '♣', '♠']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
cards = [f'{suit}{number}' for suit in suits for number in numbers]
"""
cards = []
for suit in suits:
    for number in numbers:
        cards.append(f'{suit}{number}')
"""
random.shuffle(cards)
dealer_cards = [cards.pop() for _ in range(2)]
player_cards = [cards.pop() for _ in range(2)]

print('あなたの手札は' + str(player_cards) + 'です')


def numbering_cards(cards):
    values = []
    for card in cards:
        rank  = card[1:]
        if rank == 'A':
            values.append(1)
        elif rank in ['J', 'Q', 'K']:
            values.append(10)
        else:
            values.append(int(rank))
    return sum(values)

player_num = numbering_cards(player_cards)
print(player_num)

while player_num <= 16:
    player_cards.append(cards.pop())
    player_num = numbering_cards(player_cards)

print(player_cards)
print(player_num)
    

# 全て数字にする、合計を出す
# a = 1 or 11
# 10 j q k = 10

# while 手札が16以下
# なら　一枚引く

# でないなら　引かない　
#     hit or stand
#         hit 
#             一枚引く

#         stand
#             21に近いのは...勝ち負け

# """
# def stand():
#     print(your_cards)
#     print(dealer_cards)
# """

