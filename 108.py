# number: 108
# name: median-union
# difficulty: easy
# author: yousero
# date: 11.1.2026
# time: 7:39
# result: ok
import sys

def main():
  n, l = map(int, input().split())
  a = []
  for x in range(n):
    r = list(map(int, input().split()))
    a.append(r)  
  for i in range(n-1):
    for j in range(i+1, n):
      x = []
      x += a[i]
      x += a[j]
      x.sort(reverse=True)
      print(x[len(x)//2]) 

if __name__ == '__main__':
  main()
