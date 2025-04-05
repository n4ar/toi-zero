number = input()

if number.isdigit() and (1000 <= int(number) <= 9999):
    number = number[::-1]

print(number)
