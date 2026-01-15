# number: 60
# name: cubes
# difficulty: easy
# author: yousero
# date: 9.1.2026
# time: 34:30
# result: error
import sys

def main():
  n, m = map(int, input().split())
  a = [int(input()) for x in range(n)]
  b = [int(input()) for x in range(m)]
  s = set()
  a.sort()
  b.sort()
  ra = []
  rb = []
  r = False
  if len(a) > len(b):
    a, b = b, a
    r = True
  for x in a:
    if x not in s:
      if x in b:
        s.add(x)
      else:
        ra.append(x)
  rb = [x for x in b if x not in s]
  if r: 
    a, b = b, a
    ra, rb = rb, ra
  print(len(s))
  for x in sorted(s):
    print(x, end=' ')
  print()
  print(len(ra))
  for x in ra:
    print(x, end=' ')
  print()
  print(len(rb))
  for x in rb:
    print(x, end=' ')
  print()

if __name__ == '__main__':
  main()
