import sys


def main():
  n = int(input())
  l = []
  for _ in range(n):
    row = list(map(int, input().split()))
    l.append(row)
  s, e = map(int, input().split())
  x = [[s]]
  g = {s}
  r = n + 1
  while len(x) > 0:
    c = x.pop(0)
    if c[-1] == e:
      if len(c) - 1 < r:
        r = len(c) - 1
      continue
    g.add(c[-1])
    for i,k in enumerate(l[c[-1]-1]):
      if k == 1 and (i+1) not in g:
        y = c + [i+1]
        x.append(y)
  if r == n + 1:
    r = -1
  print(r)

if __name__ == '__main__':
  main()
