import re
def LongestWord(sen):
  x = re.finditer(r"([a-zA-Z]{1,}(?!  ))", sen)
  print(x)
  maxStr = ""
  max = 0
  for matchNum, match in enumerate(x, start=1):
    if(max < (match.end()-match.start())):
      max = (match.end()-match.start())
      maxStr = match.group()
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
  
  return maxStr


aa = ["as dasd asda sda sd"]
for a in aa:
  print(LongestWord(a))