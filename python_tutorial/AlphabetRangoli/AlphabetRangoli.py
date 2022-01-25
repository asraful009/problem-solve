def print_rangoli(size):
  s=""
  s+= ("-"*size + "\n") * size
  print(f"{size} x {size}")
  print(s, end="")

def main():
  r = int(input())
  for r in range(r):
    n = int(input())
    print_rangoli(n)

if __name__ == '__main__':
  main()