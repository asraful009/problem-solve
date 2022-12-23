# from #__builtins__ import open as op

def solution(x):
    # print(x)
    i = 0
    ret = ""
    while i < len(x):
        if ord(x[i]) >= ord('a') and ord(x[i]) <= ord('z'):
            index = ord(x[i]) - ord('a')
            rev = (25 - index) + ord('a')
            # print(f"{x[i]}, {index} {rev} {chr(rev)}")
            ret += "{}".format(chr(rev))
        # elif ord(x[i]) >= ord('A') and  ord(x[i]) <= ord('Z'):
        #   index = ord(x[i]) - ord('A')
        #   rev = (25 - index) + ord('A')
        #   print(f"{x[i]}, {index} {rev} {chr(rev)}")
        #   ret += f"{chr(rev)}"
        else:
            ret += "{}".format(x[i])
        i = i + 1
    # print(ret)
    return ret


a = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
print(solution(a))
