import sys


def main():
    h, w = map(int, input().split())
    l = []
    for _ in range(h):
        row = list(map(int, input().split()))        
        l.append(row)
    s = [(0, 0, [], 0)]
    m = 0
    r = []
    while len(s) > 0:
        y, x, c, p = s.pop(0)
        p += l[y][x]
        if y == h - 1 and x == w - 1:
            r.append((c, p))
            continue
        if y < h - 1:
            n = c + ['D']
            s.append((y+1, x, n, p))
        if x < w - 1:
            n = c + ['R']
            s.append((y, x+1, n, p))
    r.sort(key=lambda x: x[1], reverse=True)
    print(r[0][1])
    print(*r[0][0])


if __name__ == '__main__':
    main()
