# number: 33
# name: levenstein-distance
# difficulty: easy
# author: yousero
# date: 12.1.2026
# time: 47:16
# result: error
import sys

def main():
  s0 = input()
  s1 = input()
  m = 0
  if len(s0) > len(s1):
    s0, s1 = s1, s0
  a = []
  for c in s0:
    i = [i for i in range(len(s1)) if s1[i] == c]
    if len(i) > 0:
      a.append(i)
  s = [(i,l,0) for i,l in enumerate(a)]
  while len(s) > 0:
    i, l, d = s.pop(0)
    if (i+1) < len(a):
      n = a[i+1]
      for x in l:
        r = [y for y in n if y > x]
        s.append((i+1, r, d+1))            
    else:
      if d > m: m = d
  print(m)

if __name__ == '__main__':
  main()
