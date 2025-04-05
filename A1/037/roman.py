def int_to_roman(n):
    roman = ""
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    for i in range(len(val)):
        while n >= val[i]:
            roman += syms[i]
            n -= val[i]
    return roman

n = int(input())
print(int_to_roman(n))
