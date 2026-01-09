# number: 125
# name: fork-conclusion
# difficulty: easy
# author: yousero
# date: 4.1.2026
# time: 11:07
# result: ok
import sys

def main():
  l = list(map(int, input().split()))
  r = {'n': l[0], 'l': 0, 'r': 0}
  for x in l[1:]:
    if x == 0: break
    t = r
    while True:
      k = ''
      if x > t['n']:
        k = 'r'
      elif x < t['n']:
        k = 'l'
      else:
        break
      if t[k] == 0:
        t[k] = {'n': x, 'l': 0, 'r': 0}
      else:
        t = t[k]
  s = [r]
  a = []
  while len(s) > 0:
    x = s.pop(0)
    c = 0
    if x['l'] != 0:
      s.append(x['l'])
      c += 1
    if x['r'] != 0:
      s.append(x['r'])
      c += 1
    if c == 2:
      a.append(x['n'])
  a.sort()
  for x in a:
    print(x)
   

if __name__ == '__main__':
  main()
