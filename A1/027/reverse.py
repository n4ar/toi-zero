char = input()

if len(char) <= 5:
    char = char[::-1]
    char = char.lower()

print(char)
