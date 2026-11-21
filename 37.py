import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  r = 0
  pre = []
  for _ in range(n):
    m = 0
    a, b, c = list(map(int, input().split()))
    pre.append((a, b, c))
    if len(pre) > 2:
      a0, b0, c0 = pre[0]
      a1, b1, c1 = pre[1]
      a2, b2, c2 = pre[2]
      pre = []
      m = a0 + a1 + a2
      if c0 < m:
        m = c0
      if (b0 + a2) < m:
        m = b0
        pre = [(a2, b2, c2)]
      if (a0 + b1) < m:
        m = a0
        pre = [(a1, b1, c1), (a2, b2, c2)]
    r += m
  if len(pre) > 0:
    if len(pre) == 1:
      m = pre[0][0]
    elif len(pre) == 2:
      a0, b0, c0 = pre[0]
      a1, b1, c1 = pre[1]
      m = a0 + a1
      if b0 < m:
        m = b0
    elif len(pre) == 3:
      a0, b0, c0 = pre[0]
      a1, b1, c1 = pre[1]
      a2, b2, c2 = pre[2]
      m = a0 + a1 + a2
      if c0 < m:
        m = c0
      if b0 < m:
        m = b0
      if (a0 + b1) < m:
        m = a0 + b1      
    r += m
  print(r)

if __name__ == '__main__':
  main()
