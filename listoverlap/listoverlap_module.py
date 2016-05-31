def listoverlap(list1, list2):
    combine_list = list(set(list1).intersection(list2))
    return(combine_list)


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = listoverlap(a, b)
    print (c)
    return c


if __name__ == '__main__':
    main()
