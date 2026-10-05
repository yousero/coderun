import sys
import functools

def main():
  n = input()
  s = input()
  w = input()
  e = input()
  u = input()
  d = input()
  o = {
    'N': n,
    'S': s,
    'W': w,
    'E': e,
    'U': u,
    'D': d,
  }
  a, b = input().split()
  b = int(b)
  @functools.cache
  def f(a, b):
    c = 1
    if b > 1:
      b -= 1
      if b > 0:
        c += sum([f(m, b) for m in o[a]])
    return c  
  print(f(a, b))


if __name__ == '__main__':
  main()
