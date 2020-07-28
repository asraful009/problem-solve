import re

if __name__ == '__main__':
    lineNumber = int(input())
    # print(lineNumber)
    txt = ""
    for i in range(0, lineNumber):
        txt += input() + "\n"
    print(txt)
    # \#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})
    # (?:(?:(\#[0-9A-Za-z]{6}|\#[0-9A-Za-z]{3})))[ ]*[;,\)]
    p = re.compile(r"(?:(\#[0-9A-Za-z]{6}|\#[0-9A-Za-z]{3}))[ ]*[;,\)]", re.M)
    print(p)
    m = p.match(txt)

    # g = m.group()
    print("{} {} ".format(m, 1))
