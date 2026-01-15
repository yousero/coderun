# number: 124
# name: leaf-conclusion
# difficulty: easy
# author: yousero
# date: 11.1.2026
# time: 14:28
# result: ok
import sys

def main():
  l = list(map(int, input().split()))
  r = {'n': l[0], 'l': 0, 'r': 0}
  for x in l:
    if x == 0: break
    t = r
    while True:
      k = ''
      n = t['n']
      if x > n:
        k = 'r'
      elif x < n:
        k = 'l'
      else:
        break
      if t[k] == 0:
        t[k] = {'n': x, 'l': 0, 'r': 0}
        break
      t = t[k]
  s = [r]
  z = []
  while len(s) > 0:
    x = s.pop()
    c = 0
    if x['l'] != 0:
      s.append(x['l'])
      c += 1
    if x['r'] != 0:
      s.append(x['r'])
      c += 1
    if c == 0:
      z.append(x['n'])
  z.sort()
  for x in z:
    print(x)
    

if __name__ == '__main__':
  main()
