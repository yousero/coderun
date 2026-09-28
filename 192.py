import sys


def main():
  l = [int(x) for x in input().split()]
  r = 0
  for i in range(1, len(l) - 1):
    x = l[i]
    a = l[i-1]
    b = l[i+1]
    if x > a and x > b:
      r += 1
  print(r)


if __name__ == '__main__':
  main()
