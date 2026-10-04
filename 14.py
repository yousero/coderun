import sys


def main():
  n, m, s, t, q = map(int, input().split())
  l = [[0 for _ in range(m)] for _ in range(n)]
  r = []
  for _ in range(q):
    x, y = map(int, input().split())
    dx, dy = abs(x - s), abs(y - t)
    a = 0
    r.append(a)
  if r:
    print(r)
  else:
    print(-1)


if __name__ == '__main__':
  main()
