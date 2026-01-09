# number: 143
# name: sorting-of-wagons-lite
# difficulty: easy
# author: yousero
# date: 5.1.2026
# time: 24:09
# result: error
import sys

def main():
  n = int(input())
  l = list(map(int, input().split()))
  f = True
  pre = None
  for x in l:
    if pre is None:
      pre = x
      continue
    if f == (pre < x):
      f = False
      break
    f = pre > x
    pre = x
  g = n % 2 == 0
  if g: f = not f
  print('YES' if f else 'NO')

if __name__ == '__main__':
  main()
