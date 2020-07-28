if __name__ == '__main__':
    arrV = []
    arrN = []
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arrV.append(score)
        arrN.append(name)
        arr.append({'n': name, 's':score})
    arrV.sort()
    # print(arrV)
    aa = arrV[0]
    for v in arrV:
        # print("{}".format(v, aa))
        if v != aa:
            break
    a = []
    for ar in arr:
        # print(ar)
        if v == ar['s']:
            a.append(ar['n'])
    a.sort()
    print("\n".join(a))
