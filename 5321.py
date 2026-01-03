import sys


def main():
  k = int(input())
  x = (1 - 2**k)/(1 - 2)
  print(int(x))

if __name__ == '__main__':
  main()
