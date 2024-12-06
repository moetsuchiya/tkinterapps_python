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
            choose_a = int(input('1 or 11?'))
            if choose_a == 1:
                values.append(1)
            elif choose_a == 11:
                values.append(11)
            else:
                print('１か１１を選んでください！')
        elif rank in ['J', 'Q', 'K']:
            values.append(10)
        else:
            values.append(int(rank))
    return sum(values)

player_num = sum_cards(player_cards) #プレイヤーの合計
dealer_num = sum_cards(player_cards) #ディーラーの合計
print('あなたの手札の合計は' + str(player_num) + 'です')

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

# while player_num <= 16:
#     player_cards.append(cards.pop()) #手札が16以下なら、一枚引く
#     player_num = sum_cards(player_cards)
# print(player_cards) #プレイヤーのカード一覧
# print('手札の合計は' + str(player_num))
    
hit_or_stand = input('HIT or STAND')
if hit_or_stand == 'HIT':
    player_cards.append(cards.pop()) #HITを選択したら、一枚引く
    if player_num < 21:
        print(player_cards)
        player_num = sum_cards(player_cards)
        print('あなたの手札の合計は' + str(player_num) + 'です')
        print('負けです')
    else:
        print(player_cards)
        player_num = sum_cards(player_cards)
        print('あなたの手札の合計は' + str(player_num) + 'です')

        hit_or_stand = input('HIT or STAND')
elif hit_or_stand == 'STAND':
    win_lose(player_num, dealer_num)