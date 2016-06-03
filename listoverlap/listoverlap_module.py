import random
from random import randint

def listoverlap(list1, list2):
    combine_list = list(set(list1).intersection(list2))
    return(combine_list)


def main():
    a = [random.randint(1, 20)for r in range(15)]
    b = [random.randint(1, 20)for r in range(15)]
    c = listoverlap(a, b)
    print(c)
    return c


if __name__ == '__main__':
    main()
