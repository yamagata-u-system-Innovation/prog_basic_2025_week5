import random

MAX_TRIES = 7


def ask_int(prompt: str) -> int:
    """整数を入力させる。失敗時は再入力を求める"""
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("整数を入力してください。")


def play() -> None:
    """数あてゲーム本体"""
    # ★ テスト側で module.random が差し替えられる前提なので、
    #    必ず module 内の random.randint を直接使う
    answer = random.randint(1, 100)
    tries = 0
    print("1〜100の数を当ててください！")

    while tries < MAX_TRIES:
        guess = ask_int("予想した数: ")
        tries += 1

        if guess == answer:
            print(f"正解！{tries}回で当たりました！")
            return
        elif guess < answer:
            print("もっと大きいです。")
        else:
            print("もっと小さいです。")

    print(f"残念！正解は {answer} でした。")


def main():
    play()


if __name__ == "__main__":
    main()
