# number: 145
# name: queue-with-error-protection
# difficulty: easy
# author: yousero
# date: 9.1.2026
# time: 8:04
# result: ok
import sys

def main():
  l = []
  while True:
    cmd, *args = input().split()
    match cmd:
      case 'push':
        l.append(int(args[0]))
        print('ok')
      case 'pop':
        if len(l) > 0:
          print(l.pop(0))
        else:
          print('error')
      case 'front':      
        if len(l) > 0:          
          print(l[0])
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
