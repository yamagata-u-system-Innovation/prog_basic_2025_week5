# 桁和の例
n = int(input("整数を入力: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("桁の合計:", total)
