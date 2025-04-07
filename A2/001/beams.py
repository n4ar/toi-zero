class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def direction(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    return min(p.x, r.x) <= q.x <= max(p.x, r.x) and min(p.y, r.y) <= q.y <= max(p.y, r.y)

def segments_intersect(p1, p2, p3, p4):
    o1 = direction(p1, p2, p3)
    o2 = direction(p1, p2, p4)
    o3 = direction(p3, p4, p1)
    o4 = direction(p3, p4, p2)

    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p3, p2):
        return True
    if o2 == 0 and on_segment(p1, p4, p2):
        return True
    if o3 == 0 and on_segment(p3, p1, p4):
        return True
    if o4 == 0 and on_segment(p3, p2, p4):
        return True
    return False

def main():
    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if r[0] != 0:
        r = [0] + r
        n += 1
    if b[0] != 0:
        b = [0] + b
        m += 1

    rr = []
    for i in range(n - 1):
        x1, x2 = r[i], r[i + 1]
        y1 = i % 2
        y2 = (i + 1) % 2
        rr.append((Point(x1, y1), Point(x2, y2)))

    bb = []
    for i in range(m - 1):
        x1, x2 = b[i], b[i + 1]
        y1 = i % 2
        y2 = (i + 1) % 2
        bb.append((Point(x1, y1), Point(x2, y2)))

    intersections = set()
    if r[0] == 0 and b[0] == 0:
        intersections.add((0, 0))

    for ar1, ar2 in rr:
        for ab1, ab2 in bb:
            endpoints = [(ar1, ab1), (ar1, ab2), (ar2, ab1), (ar2, ab2)]
            if any(p1.x == p2.x and p1.y == p2.y for p1, p2 in endpoints):
                for p1, p2 in endpoints:
                    if p1.x == p2.x and p1.y == p2.y:
                        intersections.add((p1.x, p1.y))
                        break
            elif segments_intersect(ar1, ar2, ab1, ab2):
                a1 = ar2.y - ar1.y
                b1 = ar1.x - ar2.x
                c1 = a1 * ar1.x + b1 * ar1.y

                a2 = ab2.y - ab1.y
                b2 = ab1.x - ab2.x
                c2 = a2 * ab1.x + b2 * ab1.y

                det = a1 * b2 - a2 * b1
                if det != 0:
                    x = (b2 * c1 - b1 * c2) / det
                    y = (a1 * c2 - a2 * c1) / det
                    intersections.add((x, y))

    print(len(intersections))

if __name__ == "__main__":
    main()
