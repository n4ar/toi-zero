temp = int(input())
unit = input().strip()

unit = unit.lower()

if unit == 'c':
    if temp <= 0:
        print("solid")
    elif temp < 100:
        print("liquid")
    else:
        print("gas")
elif unit == 'f':
    if temp <= 32:
        print("solid")
    elif temp < 212:
        print("liquid")
    else:
        print("gas")
else:
    print("unknown unit")
