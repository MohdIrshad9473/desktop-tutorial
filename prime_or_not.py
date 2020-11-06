def prime(a):
    ''' prime number of variable
        :param: int a
    '''
    if a > 1:
        for i in range(2, int(a/2)):
            if a % i == 0:
                return False
        return True
    return False


if prime(int(input("Enter any number :"))):
    print("  prime number")
else:
    print("not prime number")
