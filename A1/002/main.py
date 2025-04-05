amount = int(input())

c10 = amount // 10
amount %= 10

c5 = amount // 5
amount %= 5

c2 = amount // 2
amount %= 2

c1 = amount

print("10 =", c10)
print("5 =", c5)
print("2 =", c2)
print("1 =", c1)
