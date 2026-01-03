# number: 129
# difficulty: easy
# author: yousero
# date: 26.12.2025
# time: 18:28
import sys

def main():
  n = int(input())
  d = {}
  rd = {}
  for i in range(n-1):
    a, b = input().split()
    d[a] = b
    rd[b] = a
  l = []
  for k, v in d.items():    
    if (v, 0) not in l and v not in d:
      l.append((v, 0))
    i = 1
    while i > 0:
      if v not in d:
        break
      v = d[v]
      i += 1
    l.append((k, i))
  l.sort(key=lambda x: x[0])
  for n, r in l:
    print(n, r)

if __name__ == '__main__':
  main()
