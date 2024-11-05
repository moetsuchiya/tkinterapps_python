import random
def janken_game(): 
        count = 0
        while count < 3:
            print('３回勝つまでじゃんけん')
            print('ぐー: 0, ちょき:1, ぱー:2')
            my_hand = int(input())
            if my_hand == 0:
                print('あなたの手はぐーです')
            elif my_hand == 1:
                print('あなたの手はちょきです')
            elif my_hand == 2:
                print('あなたの手はぱーです')

            hands = [0, 1, 2]
            pc_hand = random.choice(hands)
            if pc_hand == 0:
                print('相手の手はぐーです')
            elif pc_hand == 1:
                print('相手の手はちょきです')
            elif pc_hand == 2:
                print('相手の手はぱーです')
            else:
                print('0か1か2のどれかを入力してください！')
                continue


            if my_hand == pc_hand:
                print('あいこで...')
                continue
            elif (my_hand == 0 and pc_hand == 1) or (my_hand == 1 and pc_hand == 2) or (my_hand == 2 and pc_hand == 0):
                count += 1
                print('あなたの勝ち！' + str(count) + '回目です！')
            else:
                print('負けです...残念')

janken_game()