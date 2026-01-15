# number: 147
# name: dec-with-error-protection
# difficulty: easy
# author: yousero
# date: 12.1.2026
# time: 10:21
# result: ok
import sys

def main():
  l = []
  while True:
    cmd, *args = input().split()
    match cmd:
      case 'push_front':
        n = int(args[0])
        l.insert(0, n)
        print('ok')
      case 'push_back':
        n = int(args[0])
        l.append(n)
        print('ok')
      case 'pop_front':
        if len(l) > 0:
          print(l.pop(0))
        else:
          print('error')
      case 'pop_back':
        if len(l) > 0:
          print(l.pop())
        else:
          print('error')
      case 'front':
        if len(l) > 0:
          print(l[0])
        else:
          print('error')
      case 'back':
        if len(l) > 0:
          print(l[-1])
        else:
          print('error')
      case 'size':
        print(len(l))
      case 'clear':
        l.clear()
        print('ok')
      case 'exit':
        print('bye')
        break


if __name__ == '__main__':
  main()
