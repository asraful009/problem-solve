"""
#

n = int(input())
dic = {}
i= 0
while i<n:
    s = input().split(" ")
    dic[s[0]] = s[1]
    i +=1
# print(dic)

i = 0
while i < n:
    try:
        s = input()
        try:
            print("{}={}".format(s, dic[s]))
        except :
            print("Not found")
    except EOFError:
        break
    i += 1

"""


import os
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dic = []
m = 50
i = 0
while i<n:

    p = i%m
    s = input().split(" ")
    # print("{} {} {} -> {}".format(i, m, p, s))
    try:
        # print(
            not bool(dic[p])
            # )

    except:
        dic.append({})
    dic[p][s[0]] = s[1]
    # print(dic[p])
    i +=1
# print((dic))

i = 0
while i < n:
    # p = i%m
    try:
        s = input()
        # print(s)
        isFound = False
        for a in range(m):
            try:
                print("{}={}".format(s, dic[a][s]))
                isFound = True
                break
            except :
                pass
        if isFound == False:
            print("Not found")
    except EOFError:
        break
    i += 1
