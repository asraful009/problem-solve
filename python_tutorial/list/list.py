
if __name__ == '__main__':
    arr = []
    N = int(input())
    cmds = []
    for n in range(0, N):
        cmds.append(input())
    # print("{}".format("\n".join(cmds)))
    for line in cmds:
        cmd = line.split(' ')
        s = ""
        if len(cmd) == 1:
            if cmd[0] == "print":
                s = "print(arr)"
            else:
                s = 'arr.{}()'.format(cmd[0])
        if len(cmd) == 2:
            s = 'arr.{}({})'.format(cmd[0], cmd[1])
        if len(cmd) == 3:
            s = 'arr.{}({}, {})'.format(cmd[0], cmd[1], cmd[2])
        
        # print(s)
        eval(s)
