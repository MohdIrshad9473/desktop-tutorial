def prime(a):
    ''' prime number of variable
        :param: int a
        :return boolean
    '''
    if a > 1:
        for i in range(2, int(a)):
            if a % i == 0:
                return False
        return True
    return False

i = int(input("input number :"))
for num in range(2, i+1):
    if prime(num):
        print(num, end=",")