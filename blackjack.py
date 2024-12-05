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


def sum_cards(cards):
    values = []
    for card in cards: #Aを１、JQLを10にして、合計値を求める
        rank = card[1:]
        if rank == 'A':
            values.append(1)
        elif rank in ['J', 'Q', 'K']:
            values.append(10)
        else:
            values.append(int(rank))
    return sum(values)

player_num = sum_cards(player_cards) #プレイヤーの合計
dealer_num = sum_cards(player_cards) #ディーラーの合計
print('手札の合計は' + str(player_num))

while player_num <= 16:
    player_cards.append(cards.pop()) #手札が16以下なら、一枚引く
    player_num = sum_cards(player_cards)

print(player_cards) #プレイヤーのカード一覧
print('手札の合計は' + str(player_num))
    
hit_or_stand = input('HIT or STAND')
while hit_or_stand == 'HIT':
    player_cards.append(cards.pop()) #HITを選択したら、一枚引く
    
    print(player_cards)
    print('手札の合計は' + str(player_num))

    hit_or_stand = input('HIT or STAND')
    if hit_or_stand == 'STAND':
        break

def win_lose(player_num, dealer_num):
    total_player = abs(21 - player_num)
    total_dealer = abs(21 - dealer_num)
    
    print('あなたの手札の合計は' + str(player_num))
    print('ディーラーの手札の合計は' + str(dealer_num))
    if total_player > total_dealer:
        print('you win!')
    elif total_player == total_dealer:
        print('aiko')
    else:
        print('you lose')

win_lose(player_num, dealer_num)