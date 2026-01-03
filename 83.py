# number: 83
# difficulty: easy
# author: yousero
# date: 27.12.2025
# time: 5:18
import sys

def main():
  n = int(input())
  a = list(map(int, input().split()))
  m = int(input())
  b = map(int, input().split())
  for i in b:
    x = i - 1
    a[x] -= 1
  for x in a:
    print('YES' if x < 0 else 'NO')

if __name__ == '__main__':
  main()
