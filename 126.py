# number: 126
# difficulty: easy
# author: yousero
# date: 2.1.2026
# time: 35:50
import sys

def main():
  b = map(int, input().split())
  r = {'n': 0, 'l': 0, 'r': 0}
  for x in b:
    if x == 0:
      break
    t = r
    d = 0
    while True:
      if t['n'] == 0:
        t['n'] = x
        break
      else:
        k = ''
        if t['n'] > x:
          k = 'l'
        elif t['n'] < x:
          k = 'r'
        else:
          break
        if t[k] == 0:
          t[k] = {'n': x, 'l': 0, 'r': 0}
          break
        else:
          t = t[k]
      d += 1
  n = [r]
  a = []
  while len(n) > 0:
    c = n.pop(0)
    x = 0
    if c['l'] != 0:
      x += 1
      n.append(c['l'])
    if c['r'] != 0:
      x += 1
      n.append(c['r'])
    if x == 1:
      a.append(c['n'])
  a.sort()
  for x in a:
    print(x)


if __name__ == '__main__':
  main()
