if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    a = [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
    print(a)