number = int(input())
operator = input()

tens = number % 10
units = number // 10

reversed_number = tens * 10 + units

if operator == '+':
    result = number + reversed_number
    print(f"{number} + {reversed_number} = {result}")
elif operator == '*':
    result = number * reversed_number
    print(f"{number} * {reversed_number} = {result}")
elif operator == '-':
    result = number - reversed_number
    print(f"{number} - {reversed_number} = {result}")
elif operator == '/':
    result = number / reversed_number
    print(f"{number} / {reversed_number} = {result}")
else:
    print("Invalid operator")
