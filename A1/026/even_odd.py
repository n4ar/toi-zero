a = int(input())
b = int(input())
c = int(input())

even = 0
odd = 0

if a % 2 == 0:
    even += 1
else:
    odd += 1

if b % 2 == 0:
    even += 1
else:
    odd += 1

if c % 2 == 0:
    even += 1
else:
    odd += 1

print(f"even {even}")
print(f"odd {odd}")
