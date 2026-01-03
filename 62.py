import sys


def main():
  a = map(int, input().split())
  s = set(a)
  print(len(s))

if __name__ == '__main__':
  main()
