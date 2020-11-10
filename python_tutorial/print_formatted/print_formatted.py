def print_formatted(number):
    # number +=1
    s = "{0:b}".format(number)
    l = len(s)
    # print({s, l})
    for i in range(1, number+1):
        print(f'{i: >{l}} {i: >{l}o} {i: >{l}X} {i: >{l}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)