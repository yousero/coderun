# number: 144
# name: great-lineland-migration
# difficulty: easy
# author: yousero
# date: 3.1.2026
# time: 13:14
# result: error
import sys

def main():
  n = int(input())
  l = list(map(int, input().split()))
  d = {}
  for i,x in enumerate(l):
    if x in d and d[x] >= i:
      print(d[x], end=' ')
      continue
    for j in range(i+1, len(l)):
      if x > l[j]:
        d[x] = j
        print(j, end=' ')
        break
    else:
      d[x] = -1
      print('-1 ', end='')
    

if __name__ == '__main__':
  main()
