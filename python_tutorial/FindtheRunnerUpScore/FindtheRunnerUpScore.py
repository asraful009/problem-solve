if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    a = arr[0]
    for v in arr:
        if v != a:
            print(v)
            break
