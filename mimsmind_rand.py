import random

def get_randomdigit_Witt(length):
    """function initializes an empty string. number of chances through the for loop equal to length. because creating a digit
    # in the string each time through. turning into int because that how range works. range gives you a list!!!!
    # that starts at 0 and goes to the number that is in range. so it's giving up the number of times through the
    # for loop equal to length"""
    number = ""
    for n in range(int(length)):
        number += str(random.randint(0,9))
    return number # this is a string
    print number

def main():

    print get_randomdigit_Witt(2)

if __name__ == '__main__':
    main()    