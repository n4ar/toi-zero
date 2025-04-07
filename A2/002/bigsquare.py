n = int(input())
points = set()

coords = []
for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))
    points.add((x, y))

max_size = 0

for i in range(n):
    x1, y1 = coords[i]
    for j in range(i + 1, n):
        x2, y2 = coords[j]

        if abs(x1 - x2) != abs(y1 - y2):
            continue

        if (x1, y2) in points and (x2, y1) in points:
            max_size = max(max_size, abs(x1 - x2))

print(max_size)
