
def get_bullcow(next, r, digits):
    bulls = 0
    cows = 0
    random1 = r
    digits = digits
    next = next
    temp = str(random1) # need to create a temporary variable so that it doesn't check
            # same integer again and say 1 bull, 1 cow for the same integer if 
            # that integer repeats
    for i in range(digits):
        if next[i] == str(random1)[i]:
            bulls += 1
            temp = next.replace(next[i], 'a') 
        else:
            pass
    for i in range(digits):
        if next[i] in temp and next[i] != temp[i]:
            cows += 1
        else:
            pass
    print '  %i Bull(s), %i Cow(s)' % (bulls, cows)
    pass

def main():

    print get_bullcow('455', 456, 3)

if __name__ == '__main__':
    main()   