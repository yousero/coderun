# number: 55
# name: angry-pigs
# difficulty: easy
# author: yousero
# date: 12.1.2026
# time: 12:51
# result: ok
import sys

def main():
  n = int(input())
  d = {}
  for i in range(n):
    x, y = map(int, input().split())
    if x in d:
      if y not in d[x]:
        d[x].append(y)
    else:
      d[x] = [y]
  print(len(d.keys()))


if __name__ == '__main__':
  main()
