import sys


def main():
  r, c = map(int, input().split())
  s = input()
  if r < c and s in ['auto', 'heat']:
    print(c)
  elif r > c and s in ['auto', 'freeze']:
    print(c)
  else:
    print(r)

if __name__ == '__main__':
  main()
