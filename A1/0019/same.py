a = input()
b = input()
c = input()

if a == b and b == c:
    print("all the same")
elif a != b and b != c and a != c:
    print("all different")
else:
    print("neither")
