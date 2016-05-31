import random
def passwordgen():
    mypw = ""
    pw_lenght = 8
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    for i in range(pw_lenght):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]
    return(mypw)


def main():
    mypw = passwordgen()
    print("Your password is:", (mypw))
    return mypw


if __name__ == '__main__':
    main()
