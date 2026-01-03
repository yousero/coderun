import sys


def main():
  n = int(input())
  rx0 = float('-inf')
  ry0 = float('-inf')
  rx1 = float('inf')
  ry1 = float('inf')
  for i in range(n):
    x, y = map(int, input().split())
    if x > rx0:
      rx0 = x
    if x < rx1:
      rx1 = x
    if y > ry0:
      ry0 = y
    if y < ry1:
      ry1 = y
  print(rx1, ry1, rx0, ry0)
  

if __name__ == '__main__':
  main()
