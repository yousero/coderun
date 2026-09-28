import sys


def main():
  alp = '0123456789'
  f = ''.join([c for c in input() if c in alp])
  if len(f) < 11:
    f = '7495' + f
  for i in range(3):
    t = ''.join([c for c in input() if c in alp])
    if len(t) < 11:
      t = '7495' + t
    if t[1:] == f[1:]:
      print('YES')
    else:
      print('NO')


if __name__ == '__main__':
  main()
