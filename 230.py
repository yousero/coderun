import sys


def main():
  n, k = map(int, input().split())
  a = []
  for _ in range(n):
    a.append(int(input()))
  m = sum(a) // k
  w = m
  i = 2
  while m > 1:
    s = 0
    for x in a:
      s += x // m
    if s == k:
      break
    if s < k:
      m -= w // i
    else:
      m += w // i
    i += 1
  m += 1
  while m < w:
    s = 0
    for x in a:
      s += x // m
    if s != k:
      m -= 1
      break
    m += 1
  print(m)


if __name__ == '__main__':
  main()
