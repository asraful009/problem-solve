from itertools import product


a =  [int(x) for x in input().split(" ") ]
A = a # list(range(a[0], a[1]+1))
b = [int(x) for x in input().split(" ") ]
B = b #list(range(b[0], b[1]+1))
arr = list(product(A, B))
s = ""
for it in arr:
  s+= f" ({it[0]}, {it[1]})"
s=s.strip()
print(s)