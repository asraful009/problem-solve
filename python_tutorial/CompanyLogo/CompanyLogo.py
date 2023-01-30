

if __name__ == '__main__':
  s = input()
  m = {}
  for c in s:
    if c not in m:
      m[c] = 0
    m[c] += 1

  sortedArr = sorted( ((v,k) for k,v in m.items()), reverse=True)
  sortedMap = {}
  for v in sortedArr:
    if v[0] not in sortedMap:
      sortedMap[v[0]] = []
    sortedMap[v[0]].append(v[1])

  count = 0
  for k, v in sortedMap.items():
    if count > 2: break
    v.sort()
    for ele in v:
      if count > 2: break
      print("{} {}".format(ele, k))
      count += 1
  