def palindrome(pal):
    pal2 = pal.replace(" ", "")
    pal3 = pal2.lower()
    #your_input = palindrome(pal3)
    if str(pal3) == str(pal3)[::-1]:
        return True
    else:
        return False

def main():
    pal = input("Write something:")
    palin_drome = palindrome(pal)
    if palin_drome == True:
        print("Your string is a palindrome")
        return True
    else:
        print("Your string does not a palindrome")
        return False

if __name__ == '__main__':
    main()
