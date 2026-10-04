import sys


def main():
  n = int(input())
  l = list(map(int, input().split()))
  r = [l[0]]
  m = 1
  for i in range(n):
    x = l[i]
    s = [x]

    for j in range(i, n):
      y = l[j]
      if y > x:
        s.append(y)
        x = y

    z = len(s)
    
    if z > m:
      r = s
      m = z

    c = s[-1]
    x = l[i]

    for k in range(1, n):
      s = [x]
      f = False
      for j in range(i, n):
        y = l[j]
        if y > x:
          if k > 0:
            k -= 1
            if y == c:
              f = True
          else:
            s.append(y)
            x = y
      if len(s) > m:
        r = s
        z = len(s)
      if f:
        break
    if z > m:
      r = s
      m = z
  print(*r)


if __name__ == '__main__':
  main()
