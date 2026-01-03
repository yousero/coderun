# number: 151
# difficulty: easy
# author: yousero
# date: 26.12.2025
# time: 43:03
import sys

def main():
  n, k = map(int, input().split())
  r = 0
  s = []
  p = []
  n -= 1
  for i in range(min(k, n)):
    x = i + 1
    s.append([x])
  while len(s) > 0:
    c = s.pop(0)
    a = sum(c)
    if a >= n:
      r += 1
      p.append(c)
      continue
    for i in range(k):
      x = i + 1
      if (a + x) <= n:
        s.append(c + [x])
      else:
        break
  print(r, p)

if __name__ == '__main__':
  main()
