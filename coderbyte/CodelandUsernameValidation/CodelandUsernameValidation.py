
import re

def CodelandUsernameValidation(strParam):
  x = re.match(r"[a-zA-Z]{1}[a-zA-Z0-9_]{2,22}[a-zA-Z0-9]{1}", strParam)
  # print(x)
  if(x):
    return True
  return False

# keep this function call here 
a = ["abc", "a123123123213"]
for s in a:
  print(CodelandUsernameValidation(s))