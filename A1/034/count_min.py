n = int(input())

numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

min_value = min(numbers)

print(min_value)
