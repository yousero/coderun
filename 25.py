import sys


def main():
  n = int(input())
  r = 0.0
  a = list(map(int, input().split()))
  a.sort()
  n = a
  while len(n) > 1:
    n = []
    pre = None
    while len(a) > 0:      
      c = a.pop(0)
      if pre is not None:
        t = c + pre
        r += t * 0.05
        n.append(t)
        pre = None
      else:
        pre = c
    if pre is not None:
      n.insert(0, pre)
    n.sort()
    a = n
  print(f'{r:.2f}')


if __name__ == '__main__':
  main()
