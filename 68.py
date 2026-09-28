import sys
from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        l = int(input())
        for x in range(l):
            t = input()
            d[t] += 1
    b = []
    a = []
    for k in d:
        if d[k] == n:
          b.append(k)
        else:
          a.append(k)
    print(len(b))
    for x in b:
        print(x)
    print(len(a) + len(b))
    for x in a:
        print(x)    
    for x in b:
        print(x)


if __name__ == '__main__':
    main()
