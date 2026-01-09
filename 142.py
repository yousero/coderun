# number: 142
# name: postfix-entry
# difficulty: easy
# author: yousero
# date: 3.1.2026
# time: 13:56
# result: ok
import sys

def main():
  s = input().split()
  r = 0
  a = []
  for x in s:
    if x not in ['-', '+', '*']:
      a.append(int(x))
    else:      
      q = a.pop()
      p = a.pop()
      d = 0
      if x == '-':
        d = p - q
      elif x == '+':
        d = p + q
      elif x == '*':
        d = p * q
      a.append(d)
  if len(a) != 1:
    print(0)
  else:
    print(a[0])

if __name__ == '__main__':
  main()
