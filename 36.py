import sys


def main():
  l, n = map(int, input().split())
  a = [int(x) for x in input().split()]
  c = [l]
  r = 0
  for x in a:
    d = c.pop()
    r += d
    y = d - x
    c.append(x)
    c.append(y)
  print(r)


if __name__ == '__main__':
  main()
