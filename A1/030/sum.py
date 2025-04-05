n = int(input())
nums = list(map(int, input().split()))

total = 0
show = []

for i in range(n):
    a = nums[2*i]
    b = nums[2*i + 1]
    if a > b:
        total += a
        show.append(str(a))
    else:
        total += b
        show.append(str(b))

print(" + ".join(show), "=", total)
