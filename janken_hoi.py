import random

def janken_game(): 
        count = 0
        hand_selection = ["ぐー", "ちょき", "ぱー"]
        hands = [0, 1, 2]

        while count < 3:
            print('３回勝つまでじゃんけん')
            print('ぐー: 0, ちょき:1, ぱー:2 から選んでね')

            my_hand = int(input())
            print(f'選択した手は{hand_selection[my_hand]}です')

            pc_hand = random.choice(hands)
            print(f'pcの手は{hand_selection[pc_hand]}です')

            if my_hand == pc_hand:
                print('あいこで...')
                continue
            elif (my_hand == 0 and pc_hand == 1) or (my_hand == 1 and pc_hand == 2) or (my_hand == 2 and pc_hand == 0):
                count += 1
                print('あなたの勝ち！' + str(count) + '回目です！')
            else:
                print('負けです...残念')

def acchimuite_hoi():
        face_selection = ["上", "下", "右", "左"]
        faces = [0, 1, 2, 3]

        print('あっちむいて...')

        while True:
            my_face = int(input('上:0 下:1 右:2 左:3 から選んでね'))

            pc_face = random.choice(faces)
            print(f'pcの顔は{face_selection[pc_face]}です')

            if my_face == pc_face:
                print('あなたの勝ち！')
                break
            else: 
                print('もう一回')

acchimuite_hoi()

"""else:
print('0か1か2のどれかを入力してください')
continue
"""
