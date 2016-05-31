import datetime


def years(age):
    age = 100 - int(age)
    allyear = 2016 + age
    return allyear


def main():
    name = input("Enter your name:")
    year = input("Enter your age:")
    plusnum = int(input("Enter a  number:"))
    for plusnum in range(plusnum):
        print("{0} you will be 100 year old in {1}".format(name, years(year)))
    return year


    #return


if __name__ == '__main__':
    main()
