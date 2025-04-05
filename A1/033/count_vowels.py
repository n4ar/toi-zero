n = int(input())

vowels = ['A', 'E', 'I', 'O', 'U']

count = 0

for i in range(n):
    char = input().strip()
    if char in vowels:
        count += 1

print(count)
