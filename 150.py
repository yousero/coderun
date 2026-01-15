# number: 150
# name: three-blocks-row
# difficulty: easy
# author: yousero
# date: 14.1.2026
# time: 24:12
# result: error
import sys
import math
def main():
  n = int(input())
  # x = 2**n
  # y = math.ceil(n / 3)
  # for i in range(1, y):
  #   x -= 2**(n - 3*i)
  # print(x)
  r = 0
  for x in range(2**n):
    if '111' not in bin(x):
      r += 1
  print(r)


if __name__ == '__main__':
  main()
