import random

def main():
    answer = random.randint(1, 100)
    tries = 0
    max_tries = 7
    print("1〜100の数を当ててください！")

    while tries < max_tries:
        s = input("予想した数: ")

        try:
            guess = int(s)
        except ValueError:
            print("整数を入力してください。")
            continue

        tries += 1

        if guess == answer:
            print(f"正解！{tries}回で当たりました！")
            return
        elif guess < answer:
            print("もっと大きいです。")
        else:
            print("もっと小さいです。")

    print(f"残念！正解は {answer} でした。")


if __name__ == "__main__":
    main()
