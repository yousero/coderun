# number: 130
# name: histogram
# difficulty: easy
# author: yousero
# date: 13.1.2026
# time: 15:49
# result: ok
import sys

def main():
  txt = ''
  for line in sys.stdin:
    txt += line
  d = {}
  for c in txt:
    if c in [' ', '\n']: continue
    if c in d:
      d[c] += 1
    else:
      d[c] = 1
  m = 0
  h = []
  for k,v in d.items():    
    if v > m: m = v
    h.append((k, v))
  h.sort(key=lambda x: x[0])
  for y in range(m):
    z = m - y
    for k,x in h:
      if x >= z:
        print('#', end='')
      else:
        print(' ', end='')
    print()
  for k,v in h:
    print(k, end='')
  print()

if __name__ == '__main__':
  main()
