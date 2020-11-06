def count_substring(string, sub_string):
    countSub = 0
    # print(string, sub_string)
    for i in range(len(string)):
        index = string.find(sub_string, i, len(sub_string)+i)
        # print("{} {} => {}".format(i, string[i: len(sub_string)], index))
        if(index > -1):
            countSub += 1

    return countSub

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)