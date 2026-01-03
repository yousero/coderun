import sys


def main():
  n = int(input())
  l = []
  for i in range(n):
    a, b = input().split()
    l.append((a, b))
  w = input()
  for a, b in l:
    if b == w:
      a, b = b, a
    if a == w:
      print(b)
      break

if __name__ == '__main__':
  main()
