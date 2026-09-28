import sys


def main():
  n, m = map(int, input().split())
  l = []
  for _ in range(n):
    row = []
    for _ in range(m):
      row.append(0)
    l.append(row)
  s = [(0, 0)]
  while len(s) > 0:
    x, y = s.pop(0)
    l[y][x] = 1
    if x + 1 < m and y + 2 < n:
      s.append((x + 1, y + 2))
    if x + 2 < m and y + 1 < n:
      s.append((x + 2, y + 1))
  s = [(m - 1, n - 1)]
  c = 0
  while len(s) > 0:
    x, y = s.pop(0)
    if l[y][x] == 2:
      c += 1
      continue
    if l[y][x] == 1:
      l[y][x] = 2
    if x - 1 > 0 and y - 2 > 0:
      s.append((x - 1, y - 2))
    if x - 2 > 0 and y - 1 > 0:
      s.append((x - 2, y - 1))
  print(c)


if __name__ == '__main__':
  main()
