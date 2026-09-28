import sys


def main():
  w0, h0, w1, h1 = map(int, input().split())
  if max(w0, h0) < max(w1, h1):
    w0, h0, w1, h1 = w1, h1, w0, h0
  if w0 < h0:
    w0, h0 = h0, w0
  if w1 < h1:
    w1, h1 = h1, w1
  l = [
    (w0, h0 + w1),
    (h0, w0 + h1),
  ]
  p = [
    l[x][0] * l[x][1]
    for x in range(2)
  ]
  o = p.index(min(p))
  print(*l[o])

if __name__ == '__main__':
  main()

