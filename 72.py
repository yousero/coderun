import sys
from collections import defaultdict

d = defaultdict(lambda: 0)

def main():
  for t in sys.stdin:
    l = t.split()
    if not l:
      break
    match l[0]:
      case 'BALANCE':
        if l[1] in d:
          print(int(d[l[1]]))
        else:
          print('ERROR')
      case 'DEPOSIT':
        d[l[1]] += int(l[2])
      case 'WITHDRAW':
        d[l[1]] -= int(l[2])
      case 'TRANSFER':
        d[l[1]] -= int(l[3])
        d[l[2]] += int(l[3])
      case 'INCOME':
        for k in d:
          d[k] *= 1 + int(l[1]) / 100


if __name__ == '__main__':
  main()
