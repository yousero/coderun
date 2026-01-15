# number: 5316
# name: snowballs
# difficulty: easy
# author: yousero
# date: 15.1.2026
# time: 19:13
# result: error
import sys

def main():
  t = int(input())
  for i in range(t):
    a, b, c = map(int, input().split())
    x = 0
    y = 0
    f = True
    for z in [a, b, c]:
      if z == 0:
        if f: y += 1
        else: x += 1
      else:
        if f: x += 1
        else: y += 1
        f = not f
    if x > y:
      print(1)
    else:
      print(0)

if __name__ == '__main__':
  main()
