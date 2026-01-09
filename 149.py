# number: 149
# name: pyramid-sorting
# difficulty: easy
# author: yousero
# date: 5.1.2026
# time: 42:43
# result: error
import sys

def main():
  n = int(input())
  l = list(map(int, input().split()))
  r = [l[0], 0, 0]
  s = [l[0]]
  i = 0
  for x in l[1:]:
    o = 0
    t = r
    while True:
      k = -1
      if x > t[0]:
        k = 2
        o += 1
      elif x < t[0]:
        k = 1
        o -= 1
      else:
        break
      if t[k] == 0:
        t[k] = [x, 0, 0]
        break
      else:
        t = t[k]
    y = i + o
    if y < 0: y = 0
    s.insert(y, x)
    if o <= 0:
      i += 1
  for x in s:
    print(x)


if __name__ == '__main__':
  main()
