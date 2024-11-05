import random

def janken_game():     
    print('じゃんけん...')

    my_hand = int(input('ぐー: 0, ちょき:1, ぱー:2'))
    print('あなたの手は' + str(my_hand))

    hands = [0, 1, 2]
    pc_hand = random.choice(hands)
    print('相手の手は' + str(pc_hand))

    if my_hand == pc_hand:
        print('あいこで...')
        janken_game()
    elif (my_hand == 0 and pc_hand == 1) or (my_hand == 1 and pc_hand == 2) or (my_hand == 2 and pc_hand == 0):
        print('あなたの勝ち！')
    else:
        print('負けです...ざんねん')

janken_game()