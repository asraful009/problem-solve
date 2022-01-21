
import math

def dmd(n, m):
  # print([n, m])
  incre = True
  for row in range(n):
    if(math.floor(n/2.0)  == row ):
      s = ""
      l = (m-7)//2
      for dash in range(l):
        s += "-"
      s+= "WELCOME"
      for dash in range(l):
        s+= "-"
      print(s)
      incre = False
    else :
      s = ""
      # for col in range(m):
      #   s += "-"
      des = (".|."* (row if incre else n-row-1))*2+".|."
      l = (m-len(des))//2
      # print(des, l)
      s+= "-"*l + des + "-"*l
      print(s)

def main():
  # run = int(input())
  for r in range(1):
    [n, m] = [int(i) for i in input().split()]
    dmd(n, m)

if __name__ == '__main__':
  main()

