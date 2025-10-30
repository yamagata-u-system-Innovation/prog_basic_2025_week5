# 素数判定の例
n = int(input("数を入力: "))
if n < 2:
    print("素数ではありません。")
else:
    for i in range(2, n):
        if n % i == 0:
            print("素数ではありません。")
            break
    else:
        print("素数です！")
