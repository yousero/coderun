# number: 121
# name: depth-added-elements
# difficulty: easy
# author: yousero
# date: 9.1.2026
# time: 17:19
# result: ok
import sys

def main():
  l = list(map(int, input().split()))
  r = {'n': l[0], 'l': 0, 'r': 0}
  print(1)
  for x in l[1:]:
    if x == 0: break
    t = r
    d = 1
    b = False
    while True:      
      d += 1
      k = ''
      if x > t['n']:
        k = 'r'
      elif x < t['n']:
        k = 'l'
      else:
        b = True
        break
      if t[k] == 0:
        t[k] = {'n': x, 'l': 0, 'r': 0}
        break
      else:
        t = t[k]
    if not b: print(d)


if __name__ == '__main__':
  main()
