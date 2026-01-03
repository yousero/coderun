import sys

def close(w, h, x, y):
  arr = []
  if x > 0:
    arr.append((x-1, y))
  if x > 0 and y > 0:
    arr.append((x-1, y-1))
  if x > 0 and y < (h-1):
    arr.append((x-1, y+1))
  if x < (w-1):
    arr.append((x+1, y))
  if x < (w-1) and y > 0:
    arr.append((x+1, y-1))
  if x < (w-1) and y < (h-1):
    arr.append((x+1, y+1))
  if y > 0:
    arr.append((x, y-1))
  if y < (h-1):
    arr.append((x, y+1))
  return arr


def main():
  w, h, m = map(int, input().split())
  a = [[0 for y in range(h)] for x in range(w)]
  for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    a[x][y] = '*'
    for j, k in close(w, h, x, y):
      if a[j][k] != '*':
        a[j][k] += 1
  for x in a:
    for y in x:
      print(y, end=' ')
    print()
    

if __name__ == '__main__':
  main()
