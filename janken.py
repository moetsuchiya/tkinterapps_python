import random
def acchimuite_hoi(winning_person):
        face_selection = ["上", "下", "右", "左"]
        faces = [0, 1, 2, 3]

        print('あっちむいて...')

        while True:
            print('上:0 下:1 右:2 左:3 から選んでね')
            my_face = int(input())

            pc_face = random.choice(faces)
            print(f'pcの顔は{face_selection[pc_face]}です')

            if my_face == pc_face:
                print(f'{winning_person}の勝ち！')
                break
            else: 
                print('もう一回')

def janken_game(): 
        hand_selection = ["ぐー", "ちょき", "ぱー"]
        hands = [0, 1, 2]

        print('３回勝つまでじゃんけん')
        print('ぐー: 0, ちょき:1, ぱー:2 から選んでね')

        my_hand = int(input())
        print(f'選択した手は{hand_selection[my_hand]}です')

        pc_hand = random.choice(hands)
        print(f'pcの手は{hand_selection[pc_hand]}です')

        if my_hand == pc_hand:
            print('あいこで...')
        elif (my_hand == 0 and pc_hand == 1) or (my_hand == 1 and pc_hand == 2) or (my_hand == 2 and pc_hand == 0):
            print('じゃんけんに勝った!')
            acchimuite_hoi('あなた')
        else:
            print('じゃんけんに負けた!')
            acchimuite_hoi('pc')
            


janken_game()

"""else:
print('0か1か2のどれかを入力してください')
continue
"""