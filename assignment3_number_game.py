# 課題#3：数当てゲーム
import random

answer = random.randint(1, 100)
tries = 0
max_tries = 7

print("1〜100の数を当ててください！")

while tries < max_tries:
    guess = int(input("予想した数: "))
    tries += 1

    if guess == answer:
        print(f"正解！{tries}回で当たりました！")
        break
    elif guess < answer:
        print("もっと大きいです。")
    else:
        print("もっと小さいです。")

if guess != answer:
    print(f"残念！正解は {answer} でした。")
