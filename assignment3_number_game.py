# assignment3_number_game.py
# 課題#3：数当てゲーム（テンプレート）
# 仕様：
# - 1〜100の乱数を生成して当てる
# - 最大7回まで挑戦可
# - ヒント：「もっと大きいです。」「もっと小さいです。」
# - 勝敗メッセージ：正解！／残念！正解は X でした。
# - 整数以外が入力されたら再入力を促す（例：「整数を入力してください」など）

import random

def main():
    answer = random.randint(1, 100)
    tries = 0
    max_tries = 7
    print("1〜100の数を当ててください！")

    while tries < max_tries:
        s = input("予想した数: ")
        # TODO: ここで s を整数に変換し、失敗時はメッセージを出して再入力させる

        # TODO: 入力値と answer を比較し、ヒント or 正解メッセージを表示
        # guess < answer → 「もっと大きいです。」
        # guess > answer → 「もっと小さいです。」
        # guess == answer → 正解（回数も表示して終了）

        # TODO: 試行回数のカウント

    # TODO: 7回以内に当てられなかった場合の敗北メッセージ
    # 例：「残念！正解は X でした。」

if __name__ == "__main__":
    main()
